from . import Users
from django.db import models
from django.utils.translation import gettext_lazy as _


class WorkerManeger(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=Users.UserType.WORKER)


class Worker(Users):

    objects = WorkerManeger()

    class Meta:
        proxy = True
        db_table = "workers"
        verbose_name = _("worker")
        verbose_name_plural = _("workers")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = Users.UserType.WORKER
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username
