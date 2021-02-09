#!/usr/bin/env spack-python

# This is a quick script to get a list of all spack packages, and then use
# multiprocessing to download each, look for instances of a search string (e.g.,
# dlopen) and save the result to an output directory of choice.
#
# Usage:
# 1. Make sure to add the spack bin to your path
# 2. Clone the repository: git clone git@github.com:spack/spack-search.git
# 3. cd spack-search
# 4. Create an output directory for your search results: mkdir -p dlopen
# 5. Run the search with a search string, output folder:
#        python search_spack.py dlopen ./dlopen

import fnmatch
import itertools
import json
import multiprocessing
import os
from pathlib import Path
import re
import signal
import shutil
import sys
import time

from spack.spec import Spec


## Workers (not currently in use)


class ExtractionWorkers:
    def __init__(self, workers=None, show_progress=True):

        # Set a conservative number of workers
        self.workers = workers or int(multiprocessing.cpu_count() / 2) - 1
        print("Using %s workers for multiprocess." % self.workers)
        self.tasks = {}
        self.show_progress = show_progress

    def start(self):
        print("Starting spack download workers!")
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()
        self.runtime = self.runtime = self.end_time - self.start_time
        print("Ending analysis workers, runtime: %s sec" % (self.runtime))

    def add_task(self, key, func, params):
        """Given a function and a set of parameters, add the task to be processed
        with the workers. The key should be some meaningful index to be used to
        assoicate the result after run (e.g., the package name and version)
        """
        self.tasks[key] = (func, params)

    def run(self):
        """run will send a list of tasks, a tuple with arguments, through a function.
        The tasks should be added with add_task.
        """
        # Keep track of some progress for the user
        total = len(self.tasks)

        # if we don't have tasks, don't run
        if not self.tasks:
            return

        # results will also have the same key to look up
        finished = dict()
        results = []

        try:
            pool = multiprocessing.Pool(self.workers, init_worker)

            self.start()
            progress = 1
            print("Preparing %s tasks..." % total)
            for key, task in self.tasks.items():
                func, params = task
                if self.show_progress:
                    prefix = "[%s/%s] %s" % (progress, total, key)
                    print(prefix, end="\r")
                result = pool.apply_async(multi_wrapper, multi_package(func, [params]))

                # Store the key with the result
                results.append((key, result))
                progress += 1

            progress = 1
            print("Waiting for results...")
            while len(results) > 0:
                pair = results.pop()
                key, result = pair
                if self.show_progress:
                    prefix = "[%s/%s] %s" % (progress, total, key)
                    print(prefix, end="\r")
                result.wait()
                progress += 1

            self.end()
            pool.close()
            pool.join()

        except (KeyboardInterrupt, SystemExit):
            print("Keyboard interrupt detected, terminating workers!")
            pool.terminate()
            sys.exit(1)

        # If the workers throw an error, comment this to see it
        except:
            sys.exit("Error running task.")

        return finished


# Supporting functions for MultiProcess Worker
def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def multi_wrapper(func_args):
    function, kwargs = func_args
    return function(**kwargs)


def multi_package(func, kwargs):
    zipped = zip(itertools.repeat(func), kwargs)
    return zipped


## File Operations


def recursive_find(base, pattern="*.*"):
    """recursive find will yield python files in all directory levels
    below a base path.

    Arguments:
      - base (str) : the base directory to search
      - pattern: a pattern to match, defaults to *.py
    """
    for root, _, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)


def read_file(filename):
    with open(filename, "r") as filey:
        content = filey.read()
    return content


def write_json(json_obj, filename):
    with open(filename, "w") as filey:
        filey.writelines(json.dumps(json_obj, indent=4, separators=(",", ": ")))
    return filename


## Main Functions


def usage(exit=False):
    """Print the usage for the user. Optionally, exit if needed"""
    message = """Usage: You should provide a search string and output directory.
mkdir -p dlopen
                       search string  output folder
python search_spack.py dlopen         ./dlopen
"""
    if exit:
        sys.exit(message)
    print(message)


def download_package(**kwargs):
    """download a package (file, or archive) and extract to folder if an archive
    is found. Currently does not support ftp.
    """
    name = kwargs.get("name")
    version = kwargs.get("version")
    outdir = kwargs.get("outdir")
    query = kwargs.get("query")

    # Output path should correspond to package and then version
    package_dir = os.path.join(outdir, name)
    key = "%s:%s" % (name, version)
    output_file = os.path.join(package_dir, "%s.json" % key)

    # Assume we don't want to overwrite
    if os.path.exists(output_file):
        return

    # keep a lookup of matches by filename, we will also keep skipped files
    matches = {}
    skipped = []

    # concretize a spec of what we want to build, a name @version
    spec = Spec("%s @%s" % (name, version)).concretized()

    # the package instance, instantiate with spec, is essentially a class for
    # "building" the spec with the package.py recipe.
    pkg = spec.package

    # This is where the package will be staged
    # /tmp/vanessa/spack-stage/spack-stage-jasper-2.0.16-hxvmmvtnngevciz4cbphxufasdlbnyhz

    # omit this contextmanager and call pkg.stage.destroy() manually if you
    # don't want the stage automatically destroyed.
    # this is from https://gist.github.com/tgamblin/11b6279efa0e49cc0572f23c5bf163ef
    with pkg.stage:

        # this fetches (if not fetched already) and expands the source into a
        # stage directory. We could optionally do pkg.do_patch() to apply patches
        pkg.do_stage()

        # Search all files for our string
        total = 0
        for filename in recursive_find(pkg.stage.source_path):
            total += 1

            # Don't bother trying with another archive
            if re.search("([.]tar[.]gz|[.]zip|[.]bz2)$", filename):
                skipped.append(filename)
                continue

            # Ignore anything we can't read, usually is .ps or similar
            try:
                text = read_file(filename)
            except:
                skipped.append(filename)
                continue

            # If we have a match, save the whole file (there aren't many)
            # These aren't meant to be human readable
            if re.search(query, text):
                matches[filename] = text

    # Save only if there are matches
    if matches:
        print("Found %s matches for %s" % (len(matches), key))
        write_json(
            {"matches": matches, "skipped": skipped, "total_files": total}, output_file
        )

    # Clean up
    if os.path.exists(pkg.stage.source_path):
        shutil.rmtree(pkg.stage.source_path)


def clean_up(package_dir, empty_file):
    # If we parse all versions and no matches, don't keep directory
    if os.path.exists(package_dir) and len(os.listdir(package_dir)) == 0:
        Path(empty_file).touch()
        os.rmdir(package_dir)


def main():
    if len(sys.argv) < 3:
        usage(exit=True)

    # Make sure we have the search string and output
    query = sys.argv[1]
    outdir = os.path.abspath(sys.argv[2])

    # Keep a record if an entire package is empty
    empty_dir = os.path.join(outdir, ".empty")
    if not os.path.exists(empty_dir):
        os.mkdir(empty_dir)

    # Exit if the output directory does not exist
    if not os.path.exists(outdir):
        sys.exit("%s does not exist." % outdir)

    # Alert the user these first two functions are a bit slow
    print("Finding packages...")

    # All packages, not including virtuals
    packages = set(spack.repo.all_package_names(False))

    # Get metadata for each
    metadata = [spack.repo.get(name) for name in packages]

    # Prepare workers to extract!
    workers = ExtractionWorkers()
    errors = []

    # Download the source, search for the string
    for pkg in metadata:

        # Empty file marker
        empty_file = os.path.join(empty_dir, pkg.name)
        if os.path.exists(empty_file):
            print("Skipping %s, marked as empty" % pkg.name)
            continue

        # Run a worker for each version
        for version in pkg.versions:

            # Make sure we make the package directory before running
            package_dir = os.path.join(outdir, pkg.name)
            if not os.path.exists(package_dir):
                os.mkdir(package_dir)

            key = "%s:%s" % (pkg.name, version.string)
            params = {
                "name": pkg.name,
                "version": version.string,
                "query": query,
                "outdir": outdir,
            }

            # Could eventually use workers (don't seem to work)
            workers.add_task(key, download_package, params)
            try:
                print("Downloading and parsing %s" % key)
                download_package(**params)
            except:
                errors.append(params)

        # If using multiprocess, this needs to be moved to after workers.run()
        clean_up(package_dir, empty_file)

    # Get the results, save to file as we go (currently not using so easy to debug)
    # results = workers.run()


# Once we've set up the system path, run the spack main method
if __name__ == "__main__":
    main()
