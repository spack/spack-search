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

from .utils import split_list
from .models import Package, SourceFile


def get_package_names():
    return Package.objects.order_by("name").values_list("name", flat=True).distinct()


def index(request):
    return render(request, "base/index.html")


class PackagesView(generic.ListView):
    template_name = "packages/packages.html"
    context_object_name = "packages"

    def get_queryset(self):
        """Return the list of packages"""
        # Get names of packages, split into 12/2 groups
        names = get_package_names()
        per_group = max(int(len(names) / 6), 1)
        return split_list(names, per_group)


def sourcefile_detail(request, sid):
    sourcefile = get_object_or_404(SourceFile, pk=sid)
    return render(request, "sourcefile/detail.html", {"sourcefile": sourcefile})


def package_detail(request, name):
    # We can have more than one version of a package
    package_set = Package.objects.filter(name=name)
    return render(
        request,
        "packages/detail.html",
        {"package_set": package_set, "packages": get_package_names()},
    )


class ResultsView(generic.DetailView):
    model = SourceFile
    template_name = "search/results.html"


def get_filter_options(results, selected):
    """Given an elastic search result, derive unique packages and extensions
    (the filter options). We assume for now that all results are sourcefiles.
    (TODO: we currently don't have extensions in the sourcefile model)
    """
    sourcefile_ids = [
        result.object.id for result in results if isinstance(result.object, SourceFile)
    ]
    # package_ids = [result.object.id for result in results if isinstance(result.object, Package)]

    # We assume all results are sourcefiles (this might not scale well)
    counts = []
    packages = (
        SourceFile.objects.filter(id__in=sourcefile_ids)
        .order_by("package__name")
        .values_list("package__name", flat=True)
        .distinct()
    )
    # Currently not running query for counts, takes too long and needs to be
    # optimized
    return {"packages": packages}


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
