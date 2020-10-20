from django.forms import ModelForm, DateInput, DateField

from .models import Sighting

class SightingForm(ModelForm):
    #Date = DateField(input_formats = ['%m%d%y'], help_text = 'Fomat of date: mmddyy')
    class Meta:
        model = Sighting
        fields = '__all__'
