from django.shortcuts import render
from .models import List

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    my_name="Justin Wang"

    return render(request, 'about.html', {'name': my_name})
