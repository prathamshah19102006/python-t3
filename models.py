from django.db import models

# Create your models here.
class Player(models.Model):
    id=models.IntegerField()
    name=models.CharField()
    team=models.CharField()
    birthdate=models.DateField()