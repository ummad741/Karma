from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from django.contrib.auth import logout

from .models import User
from .serializers import *
# Create your views here.


class RegistrationView(APIView):
    queryset = User.objects.all()

    @swagger_auto_schema(request_body=RegistrationSrl)
    def post(self, request):
        serializer = RegistrationSrl(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(user, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginSrl)
    def post(self, request):
        serializer = LoginSrl(data=request.data)
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            user.last_login_date = timezone.now()
            user.save()
            return Response({
                "Access": str(access),
                "Refresh": str(refresh),
                "User_id": user.pk
            })
        else:
            return Response({"ERROR": "Not found user"}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            logout(request)
            return Response("success", status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
