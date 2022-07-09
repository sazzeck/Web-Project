from django.contrib import admin
from .models import Services, Worker, Customer, Location, ScheduleWork

# Register your models here.

admin.site.register(Services)
admin.site.register(Worker)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(ScheduleWork)
