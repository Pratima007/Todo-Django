from django.db import models

# Create your models here.
class Firstproject(models.Model):
    name=models.CharField(max_length=30)
    description =models.TextField()
    status =models.CharField(max_length=30)

    