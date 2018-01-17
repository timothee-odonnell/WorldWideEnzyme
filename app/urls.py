from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.main, name='main'),       
    url(r'^enzymes/(?P<label>\d\.\d{1,2}\.\d{1,2}\.\w{1,3})$',views.enzyme_page, name='enzyme_page'),       
    url(r'^cofactors$',views.cofactors_list, name='cofactors_list'),       
    url(r'^cofactors/(?P<cofactor>.*)$',views.cofactors_page, name='cofactors_page'),       
    url(r'^sendbug$', views.send_bug, name='send_bug'),
    url(r'^timeline$', views.timeline, name='timeline'),
    url(r'^timeline/data$', views.timelineData, name='timelineData'),
]
