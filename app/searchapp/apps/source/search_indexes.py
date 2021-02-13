__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "Apache-2.0 OR MIT"

from django.utils import timezone
from haystack import indexes

from .models import Package, SourceFile


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    add_date = indexes.DateTimeField(model_attr="add_date")

    # We add this for autocomplete.
    name_auto = indexes.EdgeNgramField(model_attr="name")
    version_auto = indexes.EdgeNgramField(model_attr="version")

    def get_model(self):
        return Package

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class SourceFileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    add_date = indexes.DateTimeField(model_attr="add_date")

    # We add this for autocomplete.
    text_auto = indexes.EdgeNgramField(model_attr="text")
    filename_auto = indexes.EdgeNgramField(model_attr="name")

    def get_model(self):
        return SourceFile

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
