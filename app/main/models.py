from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["name", "id"]

    def __str__(self):
        return f"{self.name}"


class Schedule(models.Model):
    worker = None
    time = None


class Location(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    class Meta:
        verbose_name = "Локация"
        verbose_name = "Локации"
        ordering = ["name", "id"]


class Worker(models.Model):
    service = models.ForeignKey(
        Services, on_delete=models.PROTECT, null=True, verbose_name="Услуга"
    )
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, null=True, verbose_name="Локация"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ["service", "location", "id", "is_active"]

    def __str__(self):
        return f"Имя: {self.first_name}; Фамилия: {self.last_name}; Услуга: {self.service}"
