from rest_framework import serializers
from django.contrib.auth.models import User


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        extra_kwargs = {"password":{'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user