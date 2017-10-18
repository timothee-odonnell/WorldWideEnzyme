from rest_framework import serializers
from app.models import Enzyme

class EnzymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enzyme
        fields = ('label','accepted_name','systematic_name','status','note','activity','comment','history')
