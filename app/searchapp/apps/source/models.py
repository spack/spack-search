import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone


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
    text = models.TextField()

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
