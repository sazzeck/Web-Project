from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("Location")
    )

    class Meta:
        db_table = "locations"
        ordering = ["id"]
        verbose_name = _("Location")
        verbose_name_plural = _("Location's")

    def __str__(self):
        return self.name
