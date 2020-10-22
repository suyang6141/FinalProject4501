from django.forms import ModelForm, DateInput, DateField

from .models import Sighting

class SightingForm(ModelForm):
    Date = DateField(input_formats = ['%m%d%y'], help_text = 'Format of date: mmddyy')
    class Meta:
        model = Sighting
        #fields = '__all__'
        fields = ['Latitude', 
                'Longitude', 
                'Unique_Squirrel_ID', 
                'Shift',
                'Date',
                'Age',
                'Primary_Fur_Color',
                'Location',
                'Specific_Location',
                'Running',
                'Chasing',
                'Climbing',
                'Eating',
                'Foraging',
                'Other_Activities',
                'Kuks',
                'Quaas',
                'Moans',
                'Tail_flags',
                'Tail_twitches',
                'Approaches',
                'Indifferent',
                'Runs_from']

