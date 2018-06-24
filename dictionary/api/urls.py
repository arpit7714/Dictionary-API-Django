from django.conf.urls import url
from django.contrib import admin
from api.views import dictionary,getmeaning

urlpatterns=[
 url(r'^dictionary/',dictionary),
 url(r'^getmeaning/$',getmeaning)
]
