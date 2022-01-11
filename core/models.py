from django.db import models

class State(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=2, unique=True)
    populations = models.IntegerField()
