from rest_framework import mixins, generics
from app.models import Enzyme, Article
from api.serializers import EnzymeSerializer, ArticleSerializer

class EnzymeList(generics.ListCreateAPIView):
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer

class EnzymeDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "label"
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
