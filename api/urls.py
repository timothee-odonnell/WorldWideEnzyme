from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^enzymes/$', views.EnzymeList.as_view(),name='enzyme-list'),
    url(r'^enzymes/(?P<label>\d\.\d{1,2}\.\d{1,2}\.\w{1,3})$', views.EnzymeDetail.as_view(),name='enzyme-detail'),
    url(r'^articles/$', views.ArticleList.as_view(),name='article-list'),
    url(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(),name='article-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
