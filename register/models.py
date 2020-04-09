from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    place = models.CharField(max_length=50)
    country = models.CharField(max_length = 50)
    