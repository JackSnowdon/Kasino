from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.

class CardDeck(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, related_name='decks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name