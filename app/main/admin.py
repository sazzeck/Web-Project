from django.contrib import admin
from .models import Worker, Location, Service, Schedule

# Register your models here.

admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(Schedule)
