from datetime import datetime
from django.db import models

# Create your models here.




class water(models.Model):
    name = models.CharField(max_length=200, default='')
    date_of_invent = models.DateField(default=datetime.now)
    def __str__(self) -> str:
        return self.name


class karta(models.Model):
    comName = models.CharField(max_length=201, default='')
    number = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return self.comName
