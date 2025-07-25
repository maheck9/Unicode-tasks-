from django.db import models

# Create your models here.

class Cocktail(models.Model) :
    name = models.CharField(max_length=1000)
    alcoholic = models.CharField(max_length=500)
    instructions = models.TextField()
    thumbnail = models.URLField()

    def __str__(self):
        return self.name