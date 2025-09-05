from rest_framework import generics, permissions
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer, UserSerializer
)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user