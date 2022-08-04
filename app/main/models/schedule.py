from django.db import models

from django.forms import ValidationError

from django.utils.translation import gettext_lazy as _


class DayOfTheWeek(models.Model):
    day = models.CharField(
        max_length=9,
        primary_key=True,
        db_index=True,
        verbose_name=_("Day"),
    )

    class Meta:
        db_table = "day_of_the_week"
        verbose_name = _("Day Of The Week")
        verbose_name_plural = _("Day of The Weeks")

    def __str__(self):
        return f"{self.day}"

    @classmethod
    def save(cls, *args, **kwargs):
        if cls.objects.count() <= 7:
            super().save(*args, **kwargs)
        raise ValidationError("Too many entries in the table \"Day Of The Week\"!")


class Schedule(models.Model):
    worker = models.ForeignKey(
        "users.Worker",
        on_delete=models.CASCADE,
        verbose_name=_("Service"),
    )

    day = models.ForeignKey(
        "DayOfTheWeek",
        on_delete=models.CASCADE,
        related_name="m2o_day",
        verbose_name=_("Day")
    )

    start_time = models.TimeField(
        verbose_name=_("Start time")
    )

    end_time = models.TimeField(
        verbose_name=_("End time")
    )

    class Meta:
        db_table = "worker_schedules"
        verbose_name = _("Worker Schedule")
        verbose_name_plural = _("Worker Schedules")
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "start_time", "end_time"],
                name="unique_time_for_worker",
            )
        ]

    def __str__(self):
        return f"{self.worker} ({self.day}: {self.start_time}-{self.end_time})"
