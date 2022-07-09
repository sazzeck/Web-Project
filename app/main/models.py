from django.db import models
from django.conf import settings

# Create your models here.

user_model = settings.AUTH_USER_MODEL


class Services(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"{self.name} | {self.parent}" if self.parent else self.name

    @classmethod
    def get_default_service(cls):
        obj, created = cls.objects.get_or_create(name="Не предостовялет услуги")
        return obj.pk


class Worker(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Пользователь",
        related_name="uworker"
    )
    service = models.ForeignKey(
        "Services",
        on_delete=models.SET_DEFAULT,
        default=Services.get_default_service,
        verbose_name="Услуга",
    )
    location = models.OneToOneField(
        "Location",
        on_delete=models.PROTECT,
        verbose_name="Локация",
        related_name="lworker",
    )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return f"{self.user} ({self.service})"


class Customer(models.Model):
    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.user}"


class Location(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return f"{self.name}"


class ScheduleWork(models.Model):
    worker = models.OneToOneField(
        "Worker", on_delete=models.CASCADE, verbose_name="Специалист"
    )
    start_work = models.TimeField(default=None, verbose_name="Начало рабочего дня")
    end_work = models.TimeField(default=None, verbose_name="Конец рабочего дня")

    class Meta:
        verbose_name = "Время работы"
        verbose_name_plural = "Время работы"

    def __str__(self):
        return f"{self.worker} ({self.start_work} - {self.end_work})"


# class Appointment(models.Model):
#     worker = models.OneToOneField(Worker, on_delete=models.PROTECT)
#     customer = models.ForeingKey(Customer, on_delete=models.PROTECT)
#     start_book = models.TimeField()
#     end_book = models.TimeField()
#     day_of_week = None
#     month = None
