from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import Profile

# Create your models here.

class CardDeck(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, related_name='decks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=255)
    value = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(13)], default=0)
    deck = models.ForeignKey(CardDeck, related_name='cards', on_delete=models.CASCADE)
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SUIT_CHOICES = [
        (CLUBS, 'Clubs'),
        (SPADES, 'Spades'),
        (HEARTS, 'Hearts'),
        (DIAMONDS, 'Diamonds'),
    ]
    suit = models.CharField(
        max_length=8,
        choices=SUIT_CHOICES,
        default=CLUBS,
    )

    def __str__(self):
        return f"{self.name} Of {self.suit}"

