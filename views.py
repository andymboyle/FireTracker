from firetracker.fires.models import State, City, Address, Department, Station, Title, Person, StoryLink, Injury, Victim, Fire, Cause

from django.shortcuts import render_to_response, redirect, get_list_or_404, get_object_or_404
import urllib
from django.conf import settings

def index(request):
    fires = Fire.objects.all().order_by('date')[:5]
    return render_to_response('index.html', {
        'fires': fires,
    })

def fire(request, address, un_id):
    fire = get_object_or_404(Fire, location__street_slug=address, id=un_id)
    return render_to_response('fire_detail.html', {
        'fire': fire,
    })

def person(request, slug, un_id):
    person = get_object_or_404(Person, name_slug=slug, id=un_id)
    return render_to_response('person_detail.html', {
        'person': person,
    })

