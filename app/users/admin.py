from django.contrib import admin
from .models import Users, Worker, Customer

# Register your models here.
admin.site.register(Users)
admin.site.register(Worker)
admin.site.register(Customer)
