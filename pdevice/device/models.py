from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse


class Device(models.Model):
    aid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    serial = models.CharField(max_length=20)
    operated = models.DateField(blank=True, null=True, default='yyyy-mm-dd')
    # operated = models.DateField(_("yyyy-mm-dd"),
    # blank=True, null=True)
    # note = models.TextField(max_length=1000)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.aid

    def get_absolute_url(self):
        return reverse("device:device-detail", kwargs={"pk": self.pk})

# Create your models here.
