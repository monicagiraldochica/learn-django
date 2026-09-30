from django.shortcuts import render
from random import randint

def index(request):
    context = {
        "num_visits": randint(1, 10)
    }
    return render(request, "index.html", context=context)