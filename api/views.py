from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from app.models import Enzyme, Article, TimelineEvent   
from api.serializers import EnzymeSerializer, ArticleSerializer, EventSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'enzymes': reverse('enzyme-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format)
    })

class EnzymeList(generics.ListAPIView):
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer

class EnzymeDetail(generics.RetrieveAPIView):
    lookup_field = "label"
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class EventList(generics.ListAPIView):
    queryset = TimelineEvent.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveAPIView):
    queryset = TimelineEvent.objects.all()
    serializer_class = EventSerializer
