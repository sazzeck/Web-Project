from django.db import models


class Location(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="Name"
    )

    city = models.CharField(
        max_length=85,
        verbose_name="City"
    )

    address = models.CharField(
        max_length=170,
        verbose_name="Address"
    )

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.name} - {self.city}, {self.address}"
