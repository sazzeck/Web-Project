from django.contrib.admin import register, ModelAdmin
from .models import Users, Worker, Customer

# Register your models here.


@register(Users)
class UsersAdmin(ModelAdmin):
    list_display = (
        "username",
        "user_type",
        "is_online",
        "is_active",
        "is_staff",
        "last_login",
        "date_joined",
    )

    list_display_links = ("username",)

    search_fields = ("username",)

    list_filter = (
        "user_type",
        "is_online",
        "is_active",
        "is_staff",
        "last_login",
    )

    list_editable = (
        "is_active",
        "is_staff",
    )

    show_full_result_count = True


@register(Worker)
class WorkerAdmin(ModelAdmin):
    list_display = (
        "username",
        "is_online",
        "last_login",
        "date_joined",
    )

    list_display_links = ("username",)

    search_fields = ("username",)

    list_filter = (
        "is_online",
        "last_login",

    )

    show_full_result_count = True


@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = (
        "username",
        "is_online",
        "last_login",
        "date_joined",
    )

    list_display_links = ("username",)

    search_fields = ("username",)

    list_filter = (
        "is_online",
        "last_login",
    )

    show_full_result_count = True
