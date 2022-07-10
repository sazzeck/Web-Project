from django.db import models
from django.conf import settings

# Create your models here.

user_model = settings.AUTH_USER_MODEL


class Services(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Service",
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    name = models.CharField(
        max_length=150,
        primary_key=True,
        verbose_name="Location"
    )

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.name}"


class Worker(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Worker",
        related_name="user_worker"
    )
    location = models.OneToOneField(
        "Location",
        on_delete=models.PROTECT,
        verbose_name="Location",
        related_name="location_worker"
    )
    service = models.ForeignKey(
        "Services",
        on_delete=models.PROTECT,
        verbose_name="Service",
    )

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"{self.user} (Service: {self.service} | Location: {self.location})"


class ScheduleWork(models.Model):
    worker = models.OneToOneField(
        "Worker",
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Worker"
    )
    start_work = models.TimeField(
        default=None,
        verbose_name="Begining of the work day"
    )
    end_work = models.TimeField(
        default=None,
        verbose_name="End of the working day"
    )

    class Meta:
        verbose_name = "Schedule Work"
        verbose_name_plural = "Schedule Work"

    def __str__(self):
        return f"{self.worker} ({self.start_work} - {self.end_work})"


class Customer(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Customer"
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.user}"


# class Appointment(models.Model):
#     customer = None,
#     worker = None,
#     start_book = None,
#     end_book = None,
