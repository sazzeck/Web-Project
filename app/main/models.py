from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.

user_model = settings.AUTH_USER_MODEL


class Location(models.Model):
    place = models.CharField(
        max_length=64,
        primary_key=True,
        verbose_name="Place"
    )

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"Location: {self.place}"


class Service(models.Model):
    location = models.OneToOneField(
        "Location",
        on_delete=models.CASCADE,
        verbose_name="Location"
    )

    service = models.CharField(
        max_length=64,
        verbose_name="Name"
    )

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.service} ({self.location})"


class Worker(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User"
        )

    service = models.ForeignKey(
        "Service",
        on_delete=models.CASCADE,
        verbose_name="Service"
    )

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"{self.user} | Service: {self.service}"


class Schedule(models.Model):
    worker = models.ForeignKey(
        "Worker",
        on_delete=models.CASCADE,
        verbose_name="Worker"
    )

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
        return f"{self.worker} | Day: {self.day_of_the_week} ({self.start_time} - {self.end_time})"
