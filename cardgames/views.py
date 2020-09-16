from django.shortcuts import render

# Create your views here.

def card_index(request):
    return render(request, "card_index.html")