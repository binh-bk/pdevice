from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Device():
    id_ = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=12)
    lon = models.CharField(max_length=12)
    city = models.CharField()
    operated = models.DateField()
    updated = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.id_
    
# Create your models here.
