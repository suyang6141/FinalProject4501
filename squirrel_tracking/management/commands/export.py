
from django.core.management.base import BaseCommand,CommandError
import datetime,csv
from squirrel_tracking.models import Sighting
import csv

class Command(BaseCommand):
    help = 'Export all data to csv file'
   
    def add_argument(self,parser):
        parser.add_argument('path', type = str)
    
    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as file_:
            #add attributes
            attributes = [Latitude,
                    Longitude,
                    Unique_Squirrel_ID,
                    Shift,
                    Date,
                    Age,
                    Primary_Fur_Color,
                    Location,
                    Specific_Location,
                    Running,
                    Chasing,
                    Climbing,
                    Eating,
                    Foraging,
                    Other_Activities,
                    Kuks,
                    Quaas,
                    Moans,
                    Tail_flags,
                    Tail_twitches,
                    Approaches,
                    Indifferent,
                    Runs_from,
                ]
            writer = csv.write(file_, quoting = csv.QUOTE_ALL)
            writer.writerow(attributes)
            for i in Sighting.objects.all():
                writer.writerow([getattr(i,name) for name in attributes])


