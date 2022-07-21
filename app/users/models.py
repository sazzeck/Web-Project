from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeOfUser(models.TextChoices):
    WORKER = "WORK", _("Worker")
    CUSTOMER = "CUST", _("Customer")


class CustomUser(AbstractUser):
    type_user = models.CharField(
        max_length=4,
        choices=TypeOfUser.choices,
        verbose_name="Type User"
    )

    def __str__(self):
        return f"{self.username} ({self.type_user})"
