from django.db import models

class Familiar(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Fecha(models.Model):
    cumpleanos = models.DateField()