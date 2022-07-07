from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name", "id"]

    def __str__(self):
        return f"{self.name} ({self.parent})" if self.parent else self.name


class Worker(models.Model):
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, null=True, verbose_name="Услуга"
    )
    location = models.ForeignKey("Location", on_delete=models.PROTECT, null=True, verbose_name="Локация")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ["service", "location", "id", "is_active"]

    def __str__(self):
        return f"{self.user} ({self.location}) - {self.service}"


class Location(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        ordering = ["name", "id"]

    def __str__(self):
        return f"{self.name}"


# class Schedule(models.Model):
#     worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
#     time = None
