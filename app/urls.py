from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.main, name='main'),       
    url(r'^enzymes/(?P<label>\d\.\d{1,2}\.\d{1,2}\.\w{1,3})$',views.enzyme_page, name='enzyme_page'),       
]
