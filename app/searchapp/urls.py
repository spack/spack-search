__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "SearchApp Admin"
admin.site.site_title = "SearchApp Admin"
admin.site.index_title = "SearchApp Admin"
admin.autodiscover()


urlpatterns = [
    path("", include("searchapp.apps.source.urls")),
    path("search/", include("haystack.urls")),
    path("admin/", admin.site.urls),
]
