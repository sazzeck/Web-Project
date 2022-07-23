from django.db import models
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):
    user = models.OneToOneField(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="user_customer",
        verbose_name="username",
    )

    class Meta:
        db_table = "workers"
        verbose_name = _("worker")
        verbose_name_plural = _("workers")
