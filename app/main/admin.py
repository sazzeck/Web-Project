from django.contrib.admin import register, display, ModelAdmin
from .models import Location


@register(Location)
class LocationAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = (
        "name",
    )

    show_full_result_count = True

    # @display(description="name")
    # def services_count(self, obj: Model):
    #     return obj.method
