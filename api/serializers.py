from rest_framework import serializers
from app.models import Enzyme, Article

class EnzymeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='enzyme-detail',lookup_field='label')
    class Meta:
        model = Enzyme
        fields = ('url','label','accepted_name','systematic_name','status','note','activity','comment','history','article_set')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    enzyme = serializers.ReadOnlyField(source='enzyme.label')
    enzyme = serializers.HyperlinkedRelatedField(many=False,read_only=True,view_name='enzyme-detail',lookup_field='label')
    class Meta:
        model = Article
        fields = ('url','enzyme','title','year','volume','first_page','last_page','editorial','edition','editor','pubmed','medline')
