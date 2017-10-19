from rest_framework import serializers
from app.models import Enzyme, Article

class EnzymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enzyme
        fields = ('label','accepted_name','systematic_name','status','note','activity','comment','history','article_set')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('enzyme','title','year','volume','first_page','last_page','editorial','edition','editor','pubmed','medline')
