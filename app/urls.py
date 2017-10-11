from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.main, name='main'),       
    url(r'^enzyme$',views.enzyme_page, name='enzyme_page'),       
]
