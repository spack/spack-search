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

from .utils import (
    split_list,
    get_next_previous_packages,
    get_package_names,
    get_filter_options,
)
from .models import Package, SourceFile


def index(request):
    return render(request, "base/index.html")


class PackagesView(generic.ListView):
    template_name = "packages/packages.html"
    context_object_name = "packages"

    def get_queryset(self):
        """Return the list of packages"""
        return get_package_names()

def sourcefile_detail(request, sid):
    sourcefile = get_object_or_404(SourceFile, pk=sid)
    return render(request, "sourcefile/detail.html", {"sourcefile": sourcefile})


def package_detail(request, name):
    # We can have more than one version of a package
    package_set = Package.objects.filter(name=name)

    # Get package names for previous and next
    packages = get_package_names()
    previous, next = get_next_previous_packages(name, packages)

    return render(
        request,
        "packages/detail.html",
        {
            "package_set": package_set,
            "packages": packages,
            "next": next,
            "previous": previous,
        },
    )


class ResultsView(generic.DetailView):
    model = SourceFile
    template_name = "search/results.html"


def custom_search(request):

    query = request.GET.get("q")
    context = {}
    if query:
        page_number = request.GET.get("page", 1)
        results = SearchQuerySet().filter(content=AutoQuery(query))

        # The user can select a subset of packages
        selected = [x for x in request.GET.get("packages", "").split(",") if x]

        # We need to get filter options from all results
        context["filter_options"] = get_filter_options(results, selected)

        # "Annotate" result objects with query and filter down to selected
        filtered = []
        for result in results:
            if selected and result.object.package.name not in selected:
                continue
            result.object.query = query
            filtered.append(result)

        context["selected"] = selected
        context["query"] = query
        context["page_number"] = page_number
        context["page"] = Paginator(
            filtered, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE
        ).get_page(page_number)

    return render(request, "search/custom_search.html", context)


def autocomplete(request):
    """TODO: autocomplete doesn't seem to be working"""
    max_items = 5
    q = request.GET.get("q")
    if q:
        sqs = SearchQuerySet().autocomplete(text_auto=q)
        results = [str(result.object) for result in sqs[:max_items]]
    else:
        results = []

    return JsonResponse({"results": results})
