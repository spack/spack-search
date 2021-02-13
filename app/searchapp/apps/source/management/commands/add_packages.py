__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

from searchapp.apps.source.models import Package, SourceFile
from searchapp.apps.source.utils import recursive_find, read_json

import re
import sys


class Command(BaseCommand):
    help = "Load package data into the application."

    def import_packages(self, data_dir):

        package_files = list(recursive_find(data_dir, "*.json"))
        self.stdout.write(
            self.style.SUCCESS("Found %s package files." % len(package_files))
        )

        # For each one, create a package, and add as a source file
        for package_file in package_files:

            # Create the Package
            package_name, version = re.sub(
                "[.]json$", "", os.path.basename(package_file)
            ).split(":", 1)
            package, _ = Package.objects.get_or_create(
                name=package_name, version=version
            )
            meta = read_json(package_file)

            # Add additional metadata
            package.total_files = meta["total_files"]
            if meta["matches"]:
                build_hash = (
                    list(meta["matches"].keys())[0]
                    .split("spack-src")[0]
                    .strip("/")
                    .split("-")[-1]
                )
                package.build_hash = build_hash
            package.save()

            # Add each source file
            sources = []
            for filename, text in meta["matches"].items():
                filepath = filename.split("spack-src")[-1].strip("/")
                sourcefile, _ = SourceFile.objects.get_or_create(
                    name=filepath, package=package, text=text
                )
                sources.append(sourcefile)

            self.stdout.write(
                self.style.SUCCESS(
                    "Added package %s version %s with %s matches."
                    % (package.name, package.version, len(sources))
                )
            )

    @staticmethod
    def already_initialized():
        if Package.objects.count() > 0:
            return True

        return False

    def add_arguments(self, parser):
        parser.add_argument("data_dir", nargs=1, type=str)

    def handle(self, *args, **options):
        if self.already_initialized():
            self.stdout.write(self.style.SUCCESS("Already imported"))
            return

        if not options["data_dir"]:
            raise CommandError("Please provide a data directory.")

        data_dir = options["data_dir"][0]
        print("Data directory: %s" % data_dir)

        # Currently only support json (can add yaml if needed)
        if not data_dir or not os.path.exists(data_dir):
            raise CommandError("%s does not exist." % data_dir)

        self.import_packages(data_dir)
        self.stdout.write(self.style.SUCCESS("Successfully imported packages."))
