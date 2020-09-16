from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *


# Create your views here.

def card_index(request):
    decks = CardDeck.objects.order_by('name')
    return render(request, "card_index.html", {"decks": decks})


# Card Deck

@login_required
def create_deck(request):
    if request.method == "POST":
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            form = deck_form.save(commit=False)
            form.created_by = request.user.profile
            form.save()
            messages.error(request, "Created {0}".format(form.name), extra_tags="alert")
            return redirect("card_index")    
    else:
        deck_form = DeckForm()
    return render(request, "create_deck.html", {"deck_form": deck_form})


@login_required
def view_deck(request, pk):
    deck = get_object_or_404(CardDeck, pk=pk)
    return render(request, "view_deck.html", {"deck": deck})


@login_required
def rename_deck(request, pk):
    deck = get_object_or_404(CardDeck, pk=pk)
    if request.method == "POST":
        deck_form = DeckForm(request.POST, instance=deck)
        if deck_form.is_valid():
            form = deck_form.save(commit=False)
            form.save()
            messages.error(request, "Renamed {0}".format(form.name), extra_tags="alert")
            return redirect("view_deck", deck.pk)    
    else:
        deck_form = DeckForm(instance=deck)
    return render(request, "rename_deck.html", {"deck_form": deck_form, "deck": deck})


@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(CardDeck, pk=pk)
    if deck.created_by == request.user.profile:
        deck.delete()
        messages.error(
            request, f"Deleted {deck}", extra_tags="alert"
        )
        return redirect(reverse("card_index"))
    else:
        messages.error(request, f"Avatar Not Yours To Delete", extra_tags="alert")
        return redirect("card_index")
    
# Card


@login_required
def create_card(request, pk):
    deck = get_object_or_404(CardDeck, pk=pk)
    if request.method == "POST":
        card_form = CardForm(request.POST)
        if card_form.is_valid():
            form = card_form.save(commit=False)
            form.deck = deck
            form.name = return_card_name(form)
            form.save()
            messages.error(request, f"Added {form} To {deck}", extra_tags="alert")
            return redirect("view_deck", deck.pk)    
    else:
        card_form = CardForm()
    return render(request, "create_card.html", {"card_form": card_form, "deck": deck})


def return_card_name(card):
    values = {0: "Joker", 1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 
            11: "Jack", 12: "Queen", 13: "King"}
    return values[card.value]


@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    deck = card.deck
    card.delete()
    messages.error(
        request, f"Deleted {card}", extra_tags="alert"
    )
    return redirect("view_deck", deck.pk)       