from rest_framework import serializers

from .models import Users


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "id",
            "username",
            "user_type",
            "is_online",
        )


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "id",
            "username",
            "user_type",
            "is_online",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
        )
