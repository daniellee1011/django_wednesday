from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    now = datetime.now()
    current_year = now.year

    return render(request, 'events/home.html', {"current_year": current_year})