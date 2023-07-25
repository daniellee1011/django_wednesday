from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponse

# Generate Text File Venue List
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.text'
    # Designate The Model
    venues = Venue.objects.all()

    # Create blank list
    lines = []
    # Loop Thu and output
    for venue in venues:
        lines.append(f'{venue}\n{venue.address}\n{venue.phone}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n')

    # lines = ['This is line 1\n',
    #          'This is line 2\n',
    #          'This is line 3\n']

    # Write To TextFile
    response.writelines(lines)
    return response

# Create your views here.

def delete_venue(request, venue_id):
    print('delete_venue function called')
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    print('delete_event function called')
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def add_event(request):
    print('add_event function called')
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        try:
            form = EventForm()
        except Exception as e:
            print(e)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})


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
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})


def list_venues(request):
    venue_list = Venue.objects.all().order_by('?')
    return render(request, 'events/venue.html', {'venue_list': venue_list})


def add_venue(request):
    print('add_venue function called')
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
    event_list = Event.objects.all().order_by('name')
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().month):
    now = datetime.now()
    current_year = now.year

    return render(request, 'events/home.html', {"current_year": current_year})
