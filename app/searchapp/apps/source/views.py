__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet

from .forms import CustomSearch
from .models import Package, SourceFile


def get_package_names():
    return Package.objects.order_by("name").values_list("name", flat=True).distinct()


class IndexView(generic.ListView):
    template_name = "source/index.html"


class PackagesView(generic.ListView):
    template_name = "source/packages.html"
    context_object_name = "packages"

    def get_queryset(self):
        """Return the list of packages"""
        return get_package_names()


def package_detail(request, name):
    # We can have more than one version of a package
    package_set = Package.objects.filter(name=name)
    return render(
        request,
        "source/detail.html",
        {"package_set": package_set, "packages": get_package_names()},
    )


class ResultsView(generic.DetailView):
    model = SourceFile
    template_name = "source/results.html"


def custom_search(request):
    form = CustomSearch(request.GET)

    context = {}
    if form.is_valid():
        page_number = request.GET.get("page")
        results = SearchQuerySet().filter(content=AutoQuery(form.cleaned_data["q"]))
        context["page"] = Paginator(
            results, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE
        ).get_page(page_number)

    context["form"] = form

    return render(request, "source/custom_search.html", context)


def autocomplete(request):
    max_items = 5
    q = request.GET.get("q")
    if q:
        sqs = SearchQuerySet().autocomplete(text_auto=q)
        results = [str(result.object) for result in sqs[:max_items]]
    else:
        results = []

    return JsonResponse({"results": results})
