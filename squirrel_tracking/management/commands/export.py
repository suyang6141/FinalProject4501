
from django.core.management.base import BaseCommand
from squirrel_tracking.models import Sighting
import csv


class Command(BaseCommand):
    help = 'Export all data to csv file'
    def add_argument(self,parser):
        parser.add_argument('path', type = str)
    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as file_:
            attributes = ['Latitude',
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
                    'Runs_from',
                ]
            writer = csv.write(file_, quoting = csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Sighting.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
            ms = f'Exporting Squirrel Sighting data to {path} ...'
            self.stdout.write(self.style.SUCCESS(ms)) 
