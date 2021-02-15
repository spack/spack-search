__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from .models import Package, SourceFile

import os
import fnmatch
import json


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


def split_list(names, chunk_size):
    return [
        names[offs : offs + chunk_size] for offs in range(0, len(names), chunk_size)
    ]


def read_file(filename):
    with open(filename, "r") as fd:
        content = fd.read()
    return content


def read_json(filename):
    return json.loads(read_file(filename))


def get_filter_options(results, selected):
    """Given an elastic search result, derive unique packages and extensions
    (the filter options). We assume for now that all results are sourcefiles.
    (TODO: we currently don't have extensions in the sourcefile model)
    """
    sourcefile_ids = [
        result.object.id for result in results if isinstance(result.object, SourceFile)
    ]
    # package_ids = [result.object.id for result in results if isinstance(result.object, Package)]

    # We assume all results are sourcefiles (this might not scale well)
    counts = []
    packages = (
        SourceFile.objects.filter(id__in=sourcefile_ids)
        .order_by("package__name")
        .values_list("package__name", flat=True)
        .distinct()
    )
    # Currently not running query for counts, takes too long and needs to be
    # optimized
    return {"packages": packages}


def get_next_previous_packages(name, packages):
    next = None
    previous = None
    for i, package in enumerate(packages):
        if package == name:
            next = packages[i + 1] if i < len(packages) else None
            previous = packages[i - 1] if i > 0 else None
    return previous, next


def get_package_names():
    return Package.objects.order_by("name").values_list("name", flat=True).distinct()
