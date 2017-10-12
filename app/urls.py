from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.main, name='main'),       
    url(r'^enzyme/(?P<label>.*)$',views.enzyme_page, name='enzyme_page'),       
]
