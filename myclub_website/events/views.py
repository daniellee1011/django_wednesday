from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm

# Create your views here.
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {'venue_list': venue_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})

def home(request, year = datetime.now().year, month = datetime.now().month):
    now = datetime.now()
    current_year = now.year

    return render(request, 'events/home.html', {"current_year": current_year})