from django.db import models

# Create your models here.
class List(models.Model):
    start_time =models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    desc = models.TextField()