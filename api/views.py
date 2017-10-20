from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from app.models import Enzyme, Article
from api.serializers import EnzymeSerializer, ArticleSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'enzymes': reverse('enzyme-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })

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
