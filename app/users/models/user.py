from users.models import CustomAbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(CustomAbstractUser):
    ...

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
