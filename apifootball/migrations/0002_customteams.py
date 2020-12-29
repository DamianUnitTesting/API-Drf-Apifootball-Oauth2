# Generated by Django 3.1.2 on 2020-12-28 01:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apifootball', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=20)),
                ('names', models.CharField(blank=True, max_length=100)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('club', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, django.core.validators.MaxValueValidator(100))])),
                ('speed', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, django.core.validators.MaxValueValidator(100))])),
                ('form', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, django.core.validators.MaxValueValidator(100))])),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, django.core.validators.MaxValueValidator(100))])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
