from django.urls import path
from .views import *

urlpatterns = [
    path('card_index/', card_index, name="card_index"),
    path('create_deck/', create_deck, name="create_deck"),
    path(r'view_deck/<int:pk>/', view_deck, name="view_deck"),
    path(r'rename_deck/<int:pk>/', rename_deck, name="rename_deck"),
    path(r'delete_deck/<int:pk>/', delete_deck, name="delete_deck"),
]