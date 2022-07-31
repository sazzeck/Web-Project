from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("Location")
    )

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return self.name


class WorkersLocation(models.Model):
    worker = models.ManyToManyField(
        "users.Worker",
        related_name="workers",
        verbose_name=_("Worker"),
    )

    location = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE,
        related_name="workers_location",
        verbose_name=_("Location"),
    )

    class Meta:
        db_table = "workers_location"
        ordering = ["location"]
        verbose_name = _("Worker's Location")
        verbose_name_plural = _("Worker's Location")

    def __str__(self):
        return f"{self.location}"
