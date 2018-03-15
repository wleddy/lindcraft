# www (main site) urls

from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    # lindcraft site
    #path(r'^[I|i]ndex', views.index ,0)),
    re_path(r'^[P|p]roducts?/(?P<prod_id>\d{0,3})/$', views.product ,name='product'),
    re_path(r'^[P|p]rices?/?$', views.prices, name='prices'),
    re_path(r'^[P|p]arking', views.parkingIntro , name='parkingIntro'),
    re_path(r'^[D|d]isplay', views.displayIntro, name='displayIntro'),
    re_path(r'^[C|c]ontact', views.contact , name='contact'),
    re_path(r'^[A|a]bout', views.about , name='about'),
    re_path(r'^$', views.index , name='index'),
    
    
]