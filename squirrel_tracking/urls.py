from django.urls import path

from . import views

app_name = 'squirrel_tracking'

urlpatterns = [
        path('map/', views.map),
        path('sightings/',views.index),
        path('sightings/<Unique_Squirrel_ID>/', views.detail, name = 'Update the sighting information'),
        path('sightings/add', views.add),
        path('sightings/stats', views.stats),

        ]

