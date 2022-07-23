from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="user_customer",
        verbose_name="username"
    )

    class Meta:
        db_table = "customers"
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
