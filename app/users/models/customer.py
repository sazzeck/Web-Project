from . import Users
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomerManeger(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=Users.UserType.CUSTOMER)


class Customer(Users):

    objects = CustomerManeger()

    class Meta:
        proxy = True
        db_table = "customers"
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = Users.UserType.CUSTOMER
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username
