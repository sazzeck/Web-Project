from django.contrib import admin
from .models import CustomUser, Worker, Customer

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Worker)
admin.site.register(Customer)
