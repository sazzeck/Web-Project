from . import CustomUser
from django.db import models


class WorkerManeger(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.UserType.WORKER)


class Worker(CustomUser):

    objects = WorkerManeger()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = CustomUser.UserType.WORKER
        return super().save(*args, **kwargs)
