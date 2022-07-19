from django.contrib import admin
from .models import Location, Service, Worker, Schedule

# Register your models here.

admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Worker)
admin.site.register(Schedule)
