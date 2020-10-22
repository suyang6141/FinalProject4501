from django.core.management.base import BaseCommand
from squirrel_tracking.models import Sighting
import csv

class Command(BaseCommand):
    help = 'Export all data to a csv file'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'w', newline='') as csvfile:
            attributes = [
                    'Latitude',
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
                    'Runs_from'
            ]
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Sighting.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
        msg=f'Exporting sighting data to {path}...Done!'
        self.stdout.write(self.style.SUCCESS(msg))
