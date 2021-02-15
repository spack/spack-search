import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

import re


class BaseModel(models.Model):
    add_date = models.DateTimeField("date published", auto_now_add=True)
    modify_date = models.DateTimeField("date modified", auto_now=True)
    total_files = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Package(BaseModel):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    build_hash = models.CharField(max_length=50)

    def __str__(self):
        return "[package:%s version %s]" % (self.name, self.version)

    def get_absolute_url(self):
        return reverse("source:results", args=(self.id,))

    class Meta:
        unique_together = (
            "name",
            "version",
        )


class SourceFile(BaseModel):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    text = models.TextField()

    @property
    def all_lines(self):
        """return all lines for a sourcefile (intended for single page detail)"""
        for lineno, line in enumerate(self.text.split("\n")):
            yield lineno, line

    @property
    def lines(self, term=None):
        """we usually want to just show lines that have the query string of interest,
        including the line numbers. We will yield results in this manner.
        """
        if hasattr(self, "query"):
            term = term or self.query
        term = term or settings.SEARCH_TERM
        for lineno, line in enumerate(self.text.split("\n")):
            if re.search(term, line, re.IGNORECASE):
                yield lineno, line

    def __str__(self):
        return "[sourcefile|%s version %s:%s]" % (
            self.package.name,
            self.package.version,
            self.name,
        )

    class Meta:
        unique_together = (
            "package",
            "name",
        )
