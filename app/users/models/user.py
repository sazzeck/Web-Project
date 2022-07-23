from users.models import CustomAbstractUser


class CustomUser(CustomAbstractUser):
    ...

    def __str__(self):
        return self.username
