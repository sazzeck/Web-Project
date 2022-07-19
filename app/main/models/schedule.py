from django.db import models
from . import DayOfTheWeekChoices


class Schedule(models.Model):
    start_time = models.TimeField(
        unique=True,
        verbose_name="Start work"
    )

    end_time = models.TimeField(
        unique=True,
        verbose_name="End work"
    )

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
