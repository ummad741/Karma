from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import User


class RegistrationSrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
        )

        if user.phone.isdigit() and len(user.phone) == 9:
            user.password = make_password(validated_data['password'])
            user.save()

            access = str(AccessToken.for_user(user))
            refresh = str(RefreshToken.for_user(user))

            return {
                "User": user.pk,
                "Access": access,
                "Refresh": refresh,
            }
        else:
            raise serializers.ValidationError(
                {"MSG": "Validate error"})
