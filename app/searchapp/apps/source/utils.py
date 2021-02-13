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


def read_file(filename):
    with open(filename, "r") as fd:
        content = fd.read()
    return content


def read_json(filename):
    return json.loads(read_file(filename))
