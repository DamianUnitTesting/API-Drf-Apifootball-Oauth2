from rest_framework import serializers
from .models import Player, User


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "names",
            "nationality",
            "club",
            "age",
            "speed",
            "form",
            "rating",
            "position",
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}
