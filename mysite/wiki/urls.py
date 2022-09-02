from django.contrib import admin
from django.urls import include, path, re_path
from .views import index, get_labels


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^get_ner/$', get_labels, name='get_ner'),
]


