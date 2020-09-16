from django import forms
from .models import *

class DeckForm(forms.ModelForm):
    
    class Meta:
        model = CardDeck
        fields = ['name']


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        exclude = ['name', 'deck']