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
# If you want to generate with more than one data folder:
#        python generate_interface.py ./dlopen,./dlsym docs
#

import json
import os
import re
import sys
import yaml

## File Operations


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


def get_template(name, lookup, library_name, has_matches):
    """We don't close the header, as we need to add languages as tags"""
    template = """---\nname: "%s"\nlayout: package\nnext_package: %s\nprevious_package: %s\nlibrary_name: %s\nmatches: %s\n""" % (
        name,
        lookup.get(name, {}).get('next'),
        lookup.get(name, {}).get('previous'),
        library_name,
        list(has_matches),
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


def include_language(language):
    """For now, only include a subset of languages. Returns true if the language
    should be included, False otherwise.
    """
    return language in [
        "python",
        "c",
        "cpp",
        "go",
        "java",
        "fortran",
        "pl",
    ]


def include_line(line, library_name):
    """Given a line, determine if we should include it based on the presence
    of dlopen, and then not being a comment
    """
    if not line or not re.search(library_name, line):
        return False

    # Skip comments
    if re.search("^([//]|[/*]|#)", line.strip()):
        return False

    return True


def filter_packages(contenders, datadir):
    """Given a list of contender packages, do an original filter and
    return a list of packages that have at least one match. We will include
    these in the site.
    """
    print("Looking at %s contenders in %s." % (len(contenders), datadir))
    packages = set()

    # Get a list of filtered down packages for the lookup
    # We determine inclusion based on having matches that pass filtering
    for package in contenders:

        if package in [".empty", ".error"]:
            continue

        # Find all package versions
        package_dir = os.path.join(datadir, package)
        package_included = False
        for package_file in os.listdir(package_dir):

            # We only need one match to include it
            if package_included:
                continue

            library_name = os.path.basename(package_dir)
            package_file = os.path.join(package_dir, package_file)
            content = read_json(package_file)

            for matchname, match in content["matches"].items():

                # need to derive language here, add code
                language = get_language(matchname)
                if not include_language(language):
                    continue

                # Only include lines that have the match
                matchlines = match.split("\n")
                for index, line in enumerate(matchlines):
                    if include_line(line, library_name):
                        package_included = True
                        packages.add(package)
                    if package_included:
                        break

    print("There are %s filtered packages." % len(packages))
    packages = list(packages)
    return sorted(packages)


def main():
    if len(sys.argv) < 3:
        usage(exit=True)

    # Make sure we have the search string and output directory
    # We accept more than one data directory and will combine results
    datadirs = [os.path.abspath(x) for x in sys.argv[1].split(",")]
    outdir = os.path.abspath(sys.argv[2])

    for dirname in [outdir] + datadirs:
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

    print("Preparing to filter packages! This may take a few moments.")

    # Create master list of contenders, a package is included if it has any
    # matches in either data directory. We keep a list of separate (by datadir)
    # to generate the next/previous buttons
    packages = set()
    lookup = {}
    for datadir in datadirs:
        print("Finding contender packages for %s..." % os.path.basename(datadir))
        contenders = os.listdir(datadir)
        filtered = filter_packages(contenders, datadir)
        [packages.add(x) for x in filtered]

        # Create a lookup of previous and next (so jekyll doesn't need to)
        lookup[datadir] = {}
        for i, package in enumerate(filtered):
            lookup[datadir][package] = {
                "next": filtered[i + 1] if i < (len(filtered) - 1) else None,
                "previous": filtered[i - 1] if i > 0 else None,
            }

    # Iterate through packages, save data and generate markdown for each
    for package in packages:

        for datadir in datadirs:

            # Find all package versions
            package_dir = os.path.join(datadir, package)

            # Skip package if it doesn't have files
            if not os.path.exists(package_dir):
                continue

            library_name = os.path.basename(datadir)
            data[library_name] = {package: {}}

            # We should be able to link to other library pages from each
            # here we generate a list of other libraries with matches
            has_matches = set()
            for otherdir in datadirs:
                other_dir = os.path.join(otherdir, package)
                if os.path.exists(other_dir) and os.listdir(other_dir):
                    has_matches.add(os.path.basename(otherdir))

            # Write the header template for the package
            header = get_template(package, lookup[datadir], library_name, has_matches)

            # Try organizing into library directory
            library_dir = os.path.join(packages_dir, library_name)
            if not os.path.exists(library_dir):
                os.mkdir(library_dir)

            output_file = "%s.md" % os.path.join(library_dir, package)

            # Skip if it already exists.
            if os.path.exists(output_file):
                continue

            print("Writing library %s for package %s" % (library_name, package))

            # To make the site render with jekyll, we can only include one version
            was_written = False

            # Keep track of languages
            languages = set()

            # Skip packages that don't have matches
            package_files = os.listdir(package_dir)
            if not package_files:
                continue

            for package_file in package_files:
                version = get_version(package_file, package)
                package_file = os.path.join(package_dir, package_file)
                content = read_json(package_file)
                data[library_name][package][version] = {
                    "total_files": content["total_files"],
                    "matches": len(content["matches"]),
                }

                # We want to include all packages data, but only one version
                if was_written:
                    continue

                # For each file, include a subset of content (only with matches)
                filecontent = ""
                paths = []
                for matchname, match in content["matches"].items():

                    # need to derive language here, add code
                    language = get_language(matchname)
                    if not include_language(language):
                        continue

                    matchpath = matchname.split("spack-src")[-1].strip("/")

                    # Only include lines that have the match. We will generate a lookup,
                    # of lines to include, and then generate from that
                    include_linenos = set()
                    matchlines = match.split("\n")
                    for index, line in enumerate(matchlines):
                        if not include_line(line, library_name):
                            continue

                        # Add lines that also include +3/-3 of context
                        [include_linenos.add(x) for x in range(index - 3, index + 3)]

                    if not include_linenos:
                        continue

                    # Include the following lines and context, within range of the content
                    include_linenos = sorted(list(include_linenos))
                    lines = [
                        "%s | %s" % (idx, matchlines[idx])
                        for idx in include_linenos
                        if idx > 0 and idx < len(matchlines)
                    ]

                    # Jekyll will get thrown off if these aren't raw
                    filecontent += "\n### " + matchpath + "\n"
                    match = "\n{% raw %}\n" + "\n".join(lines) + "\n{% endraw %}\n"

                    if language:
                        languages.add(language)

                    filecontent += "\n```%s\n%s\n```" % (language, match)
                    paths.append(matchpath)

                # At this point we know that the version has content
                if not paths or not filecontent:
                    continue
                was_written = True

                # Update data to include number of filtered matches
                data[library_name][package][version]["filtered_matches"] = len(paths)

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
