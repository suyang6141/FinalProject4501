
import csv
from django.core.management.base import BaseCommand
from squirrel_tracking.models import Sighting
from datetime import date
from dateutil import parser
import re


class Command(BaseCommand):
    help = 'Import the squirrel sightings data...'
    
    def add_arguments(self,parser):
        parser.add_argument('file_path'. help = 'file containing sighting details')
        
    def handle(self, *args, **options):
        path = kwargs['file_path']
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
        
        with open(path, 'rt') as fp:
            reader = csv.DictReader(fp)
            list_ = []
            
            
            for item in reader:
                month, day, year = pattern.match(item['Date']).groups()
                obj = Sighting()
                obj.Longitude = float(item['X'])
                obj.Latitude = float(item['Y'])
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                obj.Date = date(int(year), int(month), int(day))
                obj.Age =item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = True if item['Running'] == 'TRUE' else False
                obj.Chasing = True if item['Chasing'] == 'TRUE' else False
                obj.Climbing = True if item['Climbing'] == 'TRUE' else False
                obj.Eating = True if item['Eating'] == 'TRUE' else False
                obj.Foraging = True if item['Foraging'] == 'TRUE' else False
                obj.Other_Activities = item['Other Activities']
                obj.Kuks = True if item['Kuks'] == 'TRUE' else False
                obj.Quaas = True if item['Quaas'] == 'TRUE' else False
                obj.Moans = True if item['Moans'] == 'TRUE' else False
                obj.Tail_flags = True if item['Tail flags'] == 'TRUE' else False
                obj.Tail_twitches =  True if item['Tail twitches'] == 'TRUE' else False
                obj.Approaches = True if item['Approaches'] == 'TRUE' else False
                obj.Indifferent = True if item['Indifferent'] == 'TRUE' else False
                obj.Runs_from = True if item['Runs from'] == 'TRUE' else False
                list_.append(item['Unique Squirrel ID'])
                obj.save()


                msg = f'You are importing data from {path}'
                self.stdout.write(self.style.SUCCESS(msg))

