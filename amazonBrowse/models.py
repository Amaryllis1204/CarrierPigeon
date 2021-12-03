from django.contrib import admin
from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class AmazonGoods(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date publish')