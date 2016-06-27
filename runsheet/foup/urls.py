from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', "foup.views.index"),
    #url(r'^foup/$',"runsheet1.views.Foup_home"),
    #pattern: url(r'^hardware/$', "<app_name>.views.<function_name>"),
]