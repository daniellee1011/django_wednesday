from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm

# Create your views here.
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
      form.save()
      return redirect('list-venues')

    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})

def search_venues(request):
    if request.method == "POST":
        # searched = request.POST['searched']
        # searched = request.POST('searched')
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})

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