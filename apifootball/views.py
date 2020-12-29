from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import PlayerSerializer, CreateUserSerializer
from .models import Player, User
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests



CLIENT_ID = "Client ID"
CLIENT_SECRET = "Your Client Secret"


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    """

    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        r = requests.post(
            "http://127.0.0.1:8000/o/token/",
            data={
                "grant_type": "password",
                "username": request.data["username"],
                "password": request.data["password"],
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(["POST"])
@permission_classes([AllowAny])
def token(request):
    """
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    """
    r = requests.post(
        "http://127.0.0.1:8000/o/token/",
        data={
            "grant_type": "password",
            "username": request.data["username"],
            "password": request.data["password"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    r = requests.post(
        "http://127.0.0.1:8000/o/token/",
        data={
            "grant_type": "refresh_token",
            "refresh_token": request.data["refresh_token"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(["POST"])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    r = requests.post(
        "http://127.0.0.1:8000/o/revoke_token/",
        data={
            "token": request.data["token"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    if r.status_code == requests.codes.ok:
        return Response({"message": "token revoked"}, r.status_code)

    return Response(r.json(), r.status_code)


class PlayersViewSet(viewsets.ModelViewSet):
    """
     Simple Search Filtering
    """

    has_object_permission = [permissions.IsAuthenticated, TokenHasScope]

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "names",
        "nationality",
        "club",
        "age",
        "speed",
        "rating",
        "position",
    ]
