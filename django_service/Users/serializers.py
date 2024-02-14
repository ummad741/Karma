from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from rest_framework import serializers
from .models import User


class RegistrationSrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'lastname', 'email', 'phone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            password=make_password(validated_data['password'])
        )
        if user.phone.isdigit() and len(user.phone) == 9:
            user.save()
            access = str(AccessToken.for_user(user))
            refresh = str(RefreshToken.for_user(user))
            return {
                "user_id": user.pk,
                'Refresh': refresh,
                "Access": access
            }
        else:
            raise serializers.ValidationError({"MSG": "Validate error"})


class LoginSrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
