from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', IndexView),
    url(r'^login/$', LoginView),
    url(r'^map/$', MapView ),
    url(r'^tabular-view/$', TabularView ),
    url(r'^time-table/$', TimeTableView),
    url(r'^logout/$', LogoutView ),
    url(r'^importdata/$', importdata ),
    url(r'^dataentry/$', DataEntry ),

]
