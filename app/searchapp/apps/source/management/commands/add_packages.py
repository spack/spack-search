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

    def import_packages(self, data_dir, import_all=False):

        # Subtract 1 to account for empty directory
        number_packages = len(os.listdir(data_dir)) - 1
        package_files = list(recursive_find(data_dir, "*.json"))
        self.stdout.write(
            self.style.SUCCESS("Found %s package files." % len(package_files))
        )

        # For each one, create a package, and add as a source file
        # WARNING: Only importing one version for small example
        if not import_all:
            self.stdout.write(
                self.style.WARNING(
                    "Only importing one version for package for demo purposes"
                )
            )

        last_name = None
        count = 0
        for package_file in package_files:

            # Create the Package
            package_name, version = re.sub(
                "[.]json$", "", os.path.basename(package_file)
            ).split(":", 1)

            # Only add one version of package
            if not import_all and (package_name == last_name):
                continue

            last_name = package_name
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
            for filename, text in meta["matches"].items():
                filepath = filename.split("spack-src")[-1].strip("/")

                # We cannot add source files with string literals for null
                try:
                    sourcefile, _ = SourceFile.objects.get_or_create(
                        name=filepath, package=package, text=text
                    )
                except ValueError:
                    self.stdout.write(
                        self.style.ERROR(
                            "Issue with %s sourcefile %s, likely NUL characters."
                            % (package.name, filepath)
                        )
                    )
                    pass

            if not import_all:
                count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        "Added package %s of %s: %s version %s"
                        % (count, number_packages, package.name, package.version)
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Added package %s version %s" % (package.name, package.version)
                    )
                )

    @staticmethod
    def already_initialized():
        if Package.objects.count() > 0:
            return True

        return False

    def add_arguments(self, parser):
        parser.add_argument("data_dir", nargs=1, type=str)
        parser.add_argument("--all", default=False, action="store_true")

    def handle(self, *args, **options):
        if self.already_initialized():
            self.stdout.write(self.style.SUCCESS("Already imported"))
            return

        if not options["data_dir"]:
            raise CommandError("Please provide a data directory.")

        data_dir = options["data_dir"][0]
        import_all = options["all"]

        print("Data directory: %s" % data_dir)

        # Currently only support json (can add yaml if needed)
        if not data_dir or not os.path.exists(data_dir):
            raise CommandError("%s does not exist." % data_dir)

        self.import_packages(data_dir, import_all)
        self.stdout.write(self.style.SUCCESS("Successfully imported packages."))
