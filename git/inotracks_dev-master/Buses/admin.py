from django.contrib import admin

from Buses.models import *

admin.site.register(Bus)
admin.site.register(Location)
admin.site.register(BusParameter)
admin.site.register(Stop)
admin.site.register(TimeTable)
