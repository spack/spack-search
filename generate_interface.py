#!/usr/bin/env spack-python

# This script used to take an input file and write results to a package file,
# but in practice it produced a jekyll site that was too large for jekyll to build
# and ran out of memory. Instead, it's refactored to write base templates for
# each package, so a user of the spack-search app can easily generate a site
# to explore result data, metrics and patterns.
#
# Usage:
# 1. Clone the repository: git clone git@github.com:spack/spack-search.git
# 2. cd spack-search
# 3. Run a search with search_spack.py to generate a data folder
# 4. Create an directory for your site: mkdir -p docs
# 5. Run the script providing the data folder and jekyll root
#        python generate_interface.py ./dlopen docs

import json
import os
import re
import sys
import time
import yaml

from datetime import datetime

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


def write_file(filename, content):
    with open(filename, "w") as fd:
        fd.writelines(content)


def read_json(filename):
    return json.loads(read_file(filename))


def write_yaml(yaml_dict, filename):
    """write a dictionary to yaml file

    Arguments:
     - yaml_dict (dict) : the dict to print to yaml
     - filename (str) : the output file to write to
     - pretty_print (bool): if True, will use nicer formatting
    """
    with open(filename, "w") as filey:
        filey.writelines(yaml.dump(yaml_dict))
    return filename


# Used this to derive all file extensions
def get_extensions(packages):
    """I used this function to get a list of all extensions for get_language"""
    extensions = set()
    for package in packages:
        if package == ".empty":
            continue
        package_dir = os.path.join(datadir, package)
        for package_file in os.listdir(package_dir):
            package_file = os.path.join(package_dir, package_file)
            content = read_json(package_file)
            for x in content["matches"].keys():
                extensions.add(x.split(".")[-1])
    return extensions


## Main Functions


def usage(exit=False):
    """Print the usage for the user. Optionally, exit if needed"""
    message = """Usage: You should provide a data folder and output folder for your site.
mkdir -p docs
                       data      outdir
python search_spack.py ./dlopen  ./docs
"""
    if exit:
        sys.exit(message)
    print(message)


def get_template(name, lookup):
    """We don't close the header, as we need to add languages as tags"""
    template = (
        """---\nname: "%s"\nlayout: package\nnext_package: %s\nprevious_package: %s\n"""
        % (
            name,
            lookup[name]["next"],
            lookup[name]["previous"],
        )
    )
    return template


def get_version(package_file, package):

    return (
        package_file.split("/")[-1]
        .replace(package, "")
        .replace(":", "", 1)
        .strip(".json")
    )


def get_language(matchname):
    """given an extension, do our best guess for a language
    https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers
    """
    matchname, ext = os.path.splitext(matchname)
    ext = ext.lower().strip(".")
    if ext in ["text", "txt"]:
        return "text"
    if ext in ["py", "python", "pyi", "pyi"]:
        return "python"
    if ext in ["c", "h"]:
        return "c"
    if ext in ["cc", "hh"]:
        return "cpp"
    if ext in ["yaml", "yml"]:
        return "yaml"
    if ext in ["pl"]:
        return "pl"
    if "f90" in ext:
        return "fortran"
    if ext in ["sh", "bash"]:
        return "bash"
    if ext in ["js", "javascript", ".js.map", ".map"]:
        return "js"
    if ext in ["cmake", "go", "java", "json", "lua", "html", "jl", "m4", "ac"]:
        return ext

    # If no match, return standard text
    return ""


def main():
    if len(sys.argv) < 3:
        usage(exit=True)

    # Make sure we have the search string and output directory
    datadir = os.path.abspath(sys.argv[1])
    outdir = os.path.abspath(sys.argv[2])

    for dirname in [datadir, outdir]:
        if not os.path.exists(dirname):
            sys.exit("%s does not exist." % dirname)

    # Create _data and _packages folder
    packages_dir = os.path.join(outdir, "_staging")
    data_dir = os.path.join(outdir, "_data")
    for dirname in [packages_dir, data_dir]:
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    # We will generate a data file with counts / metrics
    data = {}

    # Read in each data file, make a collection folder, and write a markdown
    print("Finding packages...")
    packages = os.listdir(datadir)

    # Create a lookup of previous and next (so jekyll doesn't need to)
    lookup = {}
    for i, package in enumerate(packages):
        lookup[package] = {
            "next": packages[i + 1] if i < (len(packages) - 1) else None,
            "previous": packages[i - 1] if i > 0 else None,
        }

    for package in packages:

        # Skip the empty directory
        if package == ".empty":
            continue

        # Find all package versions
        package_dir = os.path.join(datadir, package)

        data[package] = {}

        # Write the header template for the package
        header = get_template(package, lookup)
        output_file = "%s.md" % os.path.join(packages_dir, package)

        # Skip if it already exists.
        if os.path.exists(output_file):
            continue

        print("Writing package %s" % package)

        # To make the site render with jekyll, we can only include one version
        first_version = True

        # Keep track of languages
        languages = set()

        for package_file in os.listdir(package_dir):

            version = get_version(package_file, package)
            package_file = os.path.join(package_dir, package_file)
            content = read_json(package_file)
            data[package][version] = {
                "total_files": content["total_files"],
                "matches": len(content["matches"]),
            }

            # We want to include all packages data, but not render to these files
            if not first_version:
                continue
            first_version = False

            # For each file, include a subset of content (only with matches)
            filecontent = ""
            paths = []
            for matchname, match in content["matches"].items():

                # need to derive language here, add code
                language = get_language(matchname)

                # Only include these languages for now
                if language not in [
                    "python",
                    "c",
                    "cpp",
                    "go",
                    "java",
                    "fortran",
                    "pl",
                ]:
                    continue

                matchpath = matchname.split("spack-src")[-1].strip("/")

                # Only include lines that have the match
                lines = []
                matchlines = match.split("\n")
                for index, line in enumerate(matchlines):
                    if not line or not re.search("dlopen", line):
                        continue

                    # Skip comments
                    if re.search("^([//]|[/*]|#)", line.strip()):
                        continue

                    lines.append("%s | %s" % (index, line))

                if not lines:
                    continue

                # Jekyll will get thrown off if these aren't raw
                filecontent += "\n### " + matchpath + "\n"
                match = "\n{% raw %}\n" + "\n".join(lines) + "\n{% endraw %}\n"

                if language:
                    languages.add(language)

                filecontent += "\n```%s\n%s\n```" % (language, match)
                paths.append(matchpath)

            if not paths:
                continue

            # Update data to include number of filtered matches
            data[package][version]["filtered_matches"] = len(paths)

            # Add languages and close header
            header += "languages: %s\n---" % list(languages)

            # Include total files with matches
            header += "\n## " + version
            header += "\n%s / %s files match, %s filtered matches.\n" % (
                len(content["matches"]),
                content["total_files"],
                len(paths),
            )

            # Add links at the top
            for path in paths:
                header += "\n - [%s](#%s)" % (
                    path,
                    path.lower().replace("/", "").replace(".", ""),
                )

            header += "\n"
            header += filecontent

        # Only write to file if we have content!
        if filecontent:
            write_file(output_file, header)

    # Generate Data file
    data_file = os.path.join(data_dir, "metrics.yml")
    write_yaml(data, data_file)


# Once we've set up the system path, run the spack main method
if __name__ == "__main__":
    main()
