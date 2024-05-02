from rest_framework import serializers
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'business_name',
            'mailing_address', 'contact_name', 'contact_title', 'phone_number'
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
