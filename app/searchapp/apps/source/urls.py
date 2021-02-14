from django.urls import path

from . import views

app_name = "source"

urlpatterns = [
    path("", views.index, name="index"),
    path("packages/", views.PackagesView.as_view(), name="packages"),
    path("package/<str:name>/", views.package_detail, name="detail"),
    path("sourcefile/<int:sid>/", views.sourcefile_detail, name="sourcefile_detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("search/", views.custom_search, name="custom-search"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]
