from django.urls import path

from . import views

app_name = 'squirrel_tracking'

urlpatterns = [
        
        path('sightings/<int:Unique_Squirrel_id>/', views.detail, name = 'detail'),
        path('sightings/', views.index, name = 'all sightings'),
        ]

