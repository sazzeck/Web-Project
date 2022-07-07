from django.contrib import admin
from .models import Services, Worker, Location

# Register your models here.
admin.site.register(Services)
admin.site.register(Worker)
admin.site.register(Location)
