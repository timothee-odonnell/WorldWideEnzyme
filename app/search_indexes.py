from haystack import indexes
from app.models import *

class EnzymeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    label = indexes.CharField(model_attr='label')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Enzyme
