from django.shortcuts import render
from datetime import datetime
from .models import Event

# Create your views here.
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})

def home(request, year = datetime.now().year, month = datetime.now().month):
    now = datetime.now()
    current_year = now.year

    return render(request, 'events/home.html', {"current_year": current_year})