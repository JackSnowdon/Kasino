from django import forms
from .models import *

class DeckForm(forms.ModelForm):
    
    class Meta:
        model = CardDeck
        fields = ['name']