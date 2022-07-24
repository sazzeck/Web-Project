from . import CustomUser
from django.db import models


class CustomerManeger(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.UserType.CUSTOMER)


class Customer(CustomUser):

    objects = CustomerManeger()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = CustomUser.UserType.CUSTOMER
        return super().save(*args, **kwargs)
