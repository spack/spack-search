from django.urls import path

from . import views

app_name = "source"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("packages/", views.PackagesView.as_view(), name="packages"),
    path("package/<str:name>/", views.package_detail, name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("custom_search/", views.custom_search, name="custom-search"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]
