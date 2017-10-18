from rest_framework import mixins, generics
from app.models import Enzyme
from api.serializers import EnzymeSerializer

class EnzymeList(generics.ListCreateAPIView):
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer

class EnzymeDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "label"
    queryset = Enzyme.objects.all()
    serializer_class = EnzymeSerializer
