from django.db import models
from users.models import CustomAbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(CustomAbstractUser):
    class UserType(models.TextChoices):
        WORKER = "W", _("Worker")
        CUSTOMER = "C", _("Customer")

    user_type = models.CharField(
        max_length=1,
        choices=UserType.choices,
        verbose_name=_("user type"),
    )

    def __str__(self):
        return f"{self.username} ({self.user_type})"

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
