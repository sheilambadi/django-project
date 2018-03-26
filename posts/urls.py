from django.conf.urls import url
from . import views

urlpatterns = [
    #^ - start with, $ ends with, r stands for route
    #goes to posts/ and loads the method index in views.py
    #later on we'll load templates
    url(r'^$', views.index, name = 'index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name = 'details'),
]