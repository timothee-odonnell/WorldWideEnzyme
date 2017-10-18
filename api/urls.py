from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^enzymes/$', views.EnzymeList.as_view()),
    url(r'^enzymes/(?P<label>.*)$', views.EnzymeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
