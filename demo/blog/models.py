from django.db import models

# Create your models here.
class post(models.Model):
    title =models.CharField(max_length=200)
    dec =models.TextField()