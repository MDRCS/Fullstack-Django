from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            """ create and return a new UserProfile """
            user = models.UserProfile(
                name=validated_data['name'],
                email=validated_data['email'],
            )

            user.set_password(validated_data['password'])
            user.save()

            return user
