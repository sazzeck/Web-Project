from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import Users
from users.serializers import UsersListSerializer, UsersDetailSerializer


class UsersListView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersListSerializer


class UsersDetailView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersDetailSerializer
