from django.db import models


class Service(models.Model):
    service = models.CharField(
        max_length=64,
        verbose_name="Name"
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.service}"
