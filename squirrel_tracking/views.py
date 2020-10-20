from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Count

from .models import Sighting
from .forms import SightingForm


# Create your views here.

def index(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'squirrel_tracking/list.html',context)

def detail(request,Unique_Squirrel_ID):
    
    sighting = get_object_or_404(Sighting,Unique_Squirrel_ID=Unique_Squirrel_ID)
    
    if request.method == 'POST': # or  'GET':
        form = SightingForm(request.POST, instance = sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings/{Unique_Squirrel_ID}')
    else:
        form = SightingForm(instance= sighting)
 
    context = {
            'form': form,
            }
    return render(request,'squirrel_tracking/update.html', context)

def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            return HttpResponse(200,"not successfully added")
    form = SightingForm()
    context = {
            'form':form, 
                }
    return render(request,'squirrel_tracking/add.html',context) 


def stats(request):
    sightings = Sighting.objects.all()
    total_num = Count(sightings)
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
            'sightings': sightings}
    return render(request, 'squirrel_tracking/map.html', context)



















