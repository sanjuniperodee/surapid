import requests
from django.conf import settings
from django.shortcuts import render, get_object_or_404

# stripe.api_key = settings.STRIPE_SECRET_KEY

def home_rus(request):
    return render(request, 'rus.html')
def home_eng(request):
    return render(request, 'index.html')
