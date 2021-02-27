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


import os
import subprocess
import sys
import time

## File Operations


def write_file(content, filename):
    with open(filename, "w") as fd:
        fd.writelines(content)


## Main Functions


def get_template(package, query, outdir):
    return """#!/bin/bash

#SBATCH --time=0-00:30:00

# Set name of job shown in squeue
#SBATCH --job-name {package}-job

# Request CPU resources
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --output=.out/{package}.out
#SBATCH --error=.err/{package}.err

# This should be added via .profile, but just in case
export PATH=$HOME/software/anaconda3/bin:$HOME/code/spack/bin:$PATH
spack python search_spack_job.py {package} {query} {outdir}""".format(
        package=package, outdir=outdir, query=query
    )


def usage(exit=False):
    """Print the usage for the user. Optionally, exit if needed"""
    message = """Usage: You should provide a search string and output directory.
mkdir -p dlopen
                       search string  output folder
spack python run_search_spack.py dlopen         ./dlopen
"""
    if exit:
        sys.exit(message)
    print(message)


def main():
    if len(sys.argv) < 3:
        usage(exit=True)

    # Make sure we have the search string and output
    query = sys.argv[1]
    outdir = os.path.abspath(sys.argv[2])

    # Exit if the output directory does not exist
    if not os.path.exists(outdir):
        sys.exit("%s does not exist." % outdir)

    # Keep a record if an entire package is empty
    empty_dir = os.path.join(outdir, ".empty")
    error_dir = os.path.join(outdir, ".error")
    for dirname in [error_dir, empty_dir]:
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    # Write a directory for jobs, output, and error
    for dirname in [".jobs", ".out", ".err"]:
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    # Alert the user these first two functions are a bit slow
    print("Finding packages...")

    # All packages, not including virtuals
    packages = set(spack.repo.all_package_names(False))

    # Get metadata for each
    metadata = [spack.repo.get(name) for name in packages]

    # Download the source, search for the string
    total = len(metadata)
    for i, pkg in enumerate(metadata):

        # Empty file marker
        empty_file = os.path.join(empty_dir, pkg.name)
        error_file = os.path.join(error_dir, pkg.name)

        if os.path.exists(empty_file):
            print("Skipping %s, marked as empty" % pkg.name)
            continue
        if os.path.exists(error_file):
            print("Skipping %s, marked as errored" % pkg.name)
            continue

        # Write job template
        outfile = os.path.abspath(os.path.join(".jobs", "package-%s.job" % (pkg.name)))
        template = get_template(package=pkg.name, query=query, outdir=outdir)
        write_file(template, outfile)

        # Submit a job to do the extraction
        print("Submitting job %s of %s for %s" % (i, total, pkg.name))
        subprocess.Popen(["sbatch", outfile])

        # Pause to not stress the scheduler
        time.sleep(0.5)


# Once we've set up the system path, run the spack main method
if __name__ == "__main__":
    main()
