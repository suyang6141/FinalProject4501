from django.shortcuts import render
from .models import Sighting

# Create your views here.

def index(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel_tracking/index.html',context)

def detail(request,Unique_Squirrel_ID):
    sighting = get_object_or_404(Sighting, pk=Unique_Squirrel_ID)
    context = {
            'sighting':sighting,
            }
    return render(request,'squirrel_tracking/detail.html', context)

