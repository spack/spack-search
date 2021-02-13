__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.contrib import admin

from .models import Package, SourceFile


class SourceFilesInline(admin.TabularInline):
    model = SourceFile
    extra = 3


class PackageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "version"]}),
        (
            "Date information",
            {"fields": ["add_date", "modify_date"], "classes": ["collapse"]},
        ),
    ]
    inlines = [SourceFilesInline]
    list_display = ("name", "version")
    list_filter = ["name", "version"]


admin.site.register(Package, PackageAdmin)
