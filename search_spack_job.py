#!/usr/bin/env spack-python

# This is a job to be run with run_search_spack.py. It should be submit with
# a template (sbatch) with a final like like:
#
#         package        version search string  output-folder
# python3 py-fenics-ffcx master dlmopen /Users/sochat1/Documents/Code/spack-search/dlmopen

import fnmatch
import json
import os
from pathlib import Path
import re
import shutil
import sys

from spack.spec import Spec

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
python3 search_spack.py dlopen         ./dlopen
"""
    if exit:
        sys.exit(message)
    print(message)


def download_package(name, version, outdir, query):
    """download a package (file, or archive) and extract to folder if an archive
    is found. Currently does not support ftp.
    """
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


def clean_up(package_dir, empty_file, success, error_file):
    """Cleaning up means figuring out if we had an error first, and then if
    there are just no results, and touching a file in the correct location.
    """

    if (
        os.path.exists(package_dir)
        and len(os.listdir(package_dir)) == 0
        and not success
    ):
        Path(error_file).touch()
        os.rmdir(package_dir)

    # If we parse all versions and no matches, don't keep directory
    elif os.path.exists(package_dir) and len(os.listdir(package_dir)) == 0:
        Path(empty_file).touch()
        os.rmdir(package_dir)


def main():
    if len(sys.argv) < 3:
        usage(exit=True)

    # Make sure we have the search string and output
    package = sys.argv[1]
    query = sys.argv[2]
    outdir = os.path.abspath(sys.argv[3])

    # Exit if the output directory does not exist
    if not os.path.exists(outdir):
        sys.exit("%s does not exist." % outdir)

    # Empty directory created by submission script
    empty_dir = os.path.join(outdir, ".empty")
    error_dir = os.path.join(outdir, ".error")

    # Empty or error file marker
    empty_file = os.path.join(empty_dir, package)
    error_file = os.path.join(error_dir, package)
    if os.path.exists(empty_file):
        print("Skipping %s, marked as empty" % package)
        sys.exit(0)
    elif os.path.exists(error_file):
        print("Skipping %s, marked as errored" % package)
        sys.exit(0)

    # Get the package
    pkg = spack.repo.get(package)
    success = False

    for version in pkg.versions:

        # Make sure we make the package directory before running
        package_dir = os.path.join(outdir, pkg.name)
        if not os.path.exists(package_dir):
            os.mkdir(package_dir)

        # Currently there is a concretion error, let's keep a record of this.
        try:
            download_package(
                name=pkg.name, version=version.string, query=query, outdir=outdir
            )
            success = True
        except:
            pass

    clean_up(package_dir, empty_file, success, error_file)


# Once we've set up the system path, run the spack main method
if __name__ == "__main__":
    main()
