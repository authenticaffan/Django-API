from django.db import models

# Create your models here.

class Details(models.Model):
    Name=models.CharField(max_length=100)
    Details=models.CharField(max_length=10000)
