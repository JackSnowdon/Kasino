from django.urls import path
from .views import *

urlpatterns = [
    path('card_index/', card_index, name="card_index"),
    path('create_deck/', create_deck, name="create_deck"),
]