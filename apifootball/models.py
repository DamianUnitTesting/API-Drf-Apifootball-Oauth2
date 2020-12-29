from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

""" Models for Football-API """


class User(AbstractUser):
    is_active = models.BooleanField(default=True)


class Player(models.Model):
    # Basic Models from Players
    position = models.CharField(max_length=20, blank=True)
    names = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    club = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    # Set of Skills
    speed = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    form = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    def __str__(self):
        return self.names


class CustomTeams(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=20, blank=True)
    names = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    club = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    # Set of Skills
    speed = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )
    form = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1, MaxValueValidator(100))]
    )

    def __str__(self):
        return self.team_name
