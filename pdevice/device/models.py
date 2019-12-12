from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Device(models.Model):
    aid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    serial = models.CharField(max_length=20)
    operated = models.DateField()
    # note = models.TextField(max_length=1000)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.aid

    def __repr__(self):
        return (self.aid, self.name)
# Create your models here.
