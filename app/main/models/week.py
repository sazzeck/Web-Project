from django.db import models
from django.utils.translation import gettext_lazy as _


class DayOfTheWeekChoices(models.TextChoices):
    MONDAY = "Mon", _("Monday")
    TUESDAY = "Tue", _("Tuesday")
    WEDNESDAY = "Wed", _("Wednesday")
    THURSDAY = "Thu", _("Thursday")
    FRIDAY = "Fri", _("Friday")
    SATURDAY = "Sat", _("Saturday")
    SUNDAY = "Sun", _("Sunday")
