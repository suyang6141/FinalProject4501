from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
#from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Count

from .models import Sighting
from .forms import SightingForm


# Create your views here.

def index(request):
    sightings = Sighting.objects.all()
    context = {
            'squirrel sightings':sightings,
            }
    return render(request,'squirrel_tracking/list.html',context)

def detail(request,Unique_Squirrel_ID):
    sighting = get_object_or_404(Sighting, pk=Unique_Squirrel_ID)
    if request.method == 'POST': # or  'GET':
        form = SightingForm(request.POST, instance = sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings/{Unique_Squirrel_ID}')
    else:
        form = SightingForm(instance= sighting)
        #return redirect('sightings/{Unique_Squirrel_ID}')
 
    context = {
            'sighting_form': form,
            }
    return render(request,'squirrel_tracking/update.html', context)

def add(request):
    if request.method == 'GET' : #or 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SightingForm()
    context = {
                'add_sighting_form':form, 
                }
    return render(request,'squirrel_tracking/add.html',context) 


def stats(request):
    sightings = Sighting.objects.all()
    total_num = count(sightings)
    latitude_stat= sightings.aggregate(minimum = Min('Latitude'),maximum = Max('Latitude'),average = Avg('Latitude'))
    longitude_stat=sightings.aggregate(minimum = Min('Longitude'),maximum = Max('Longitude'),average = Avg('Longitude'))
    shift_stat=list(sightings.values_list('Shift').annotate(Count('Shift')))
    age_stat =list(sightings.values_list('Age').annotate(Count('Age')))
    context = {
        'total_num':total_num,
        'latitude_stats' :latitude_stat,
        'longitude_stats': longitude_stat,
        'shift_stats': shift_stat,
        'age_stats':age_stat,
            }
    return render(request,'squirrel_tracking/stats.html', context)


def map(request):
    sightings = Sighting.objects.all()[:100]
    context = {
            'sighting': sightings}
    return render(request, 'squirrel_tracking/map.html', context)



















