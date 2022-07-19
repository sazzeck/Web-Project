from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


user_model = settings.AUTH_USER_MODEL


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


class Worker(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User"
        )

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"{self.user}"


class Schedule(models.Model):
    start_time = models.TimeField(
        unique=True,
        verbose_name="Start work"
    )

    end_time = models.TimeField(
        unique=True,
        verbose_name="End work"
    )

    class DayOfTheWeekChoices(models.TextChoices):
        MONDAY = "Mon", _("Monday")
        TUESDAY = "Tue", _("Tuesday")
        WEDNESDAY = "Wed", _("Wednesday")
        THURSDAY = "Thu", _("Thursday")
        FRIDAY = "Fri", _("Friday")
        SATURDAY = "Sat", _("Saturday")
        SUNDAY = "Sun", _("Sunday")

    day_of_the_week = models.CharField(
        max_length=3,
        choices=DayOfTheWeekChoices.choices,
        default=DayOfTheWeekChoices.MONDAY,
        verbose_name="Working day"
    )

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedule"

    def __str__(self):
        return f"{self.day_of_the_week} ({self.start_time} - {self.end_time})"
