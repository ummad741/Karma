from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status

from .models import User
from .serializers import *
# Create your views here.


class RegistrationView(APIView):
    queryset = User.objects.all()
    serializer = RegistrationSrl()

    @swagger_auto_schema(request_body=RegistrationSrl)
    def post(self, request):
        serializer = RegistrationSrl(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()
            return Response(user_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

