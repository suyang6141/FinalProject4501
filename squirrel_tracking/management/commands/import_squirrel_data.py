import os
import csv 
import datetime as dt
from squdata.models import Squirreldata
from django.core.management.base import BaseCommand, CommandError
import pytz #pip install pytz

# from django.utils.timezone import get_current_timezone
class Command(BaseCommand):
    help = 'read csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('squ_file',type=str) 
    
    def handle(self, *args, **options):
        def tobool(string):
            if string == 'true':
                return True
            elif string == 'false':
                return False 

        with open(options['squ_file']) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            data = list(csv_reader)
            for item in data:
                date = dt.datetime.strptime(item['Date'],'%m%d%Y')
                timezone = pytz.timezone("UTC")
                date = timezone.localize(date)

                try:
                    created = Squirreldata(
                        latitude=item['X'],
                        longitude=item['Y'],
                        unique_squirrel_id= item['Unique Squirrel ID'],
                        shift=item['Shift'],
                        date=date,
                        age = item['Age'],
                        fur_color=item['Primary Fur Color'],
                        location=item['Location'],
                        specific_location=item['Specific Location'],
                        running=tobool(item['Running']),
                        chasing=tobool(item['Chasing']),
                        climbing=tobool(item['Climbing']),
                        eating=tobool(item['Eating']),
                        foraging=tobool(item['Foraging']),
                        other_activities=item['Other Activities'],
                        kuks=tobool(item['Kuks']),
                        quaas=tobool(item['Quaas']),
                        moans=tobool(item['Moans']),
                        tail_flags=tobool(item['Tail flags']),
                        tail_twitches=tobool(item['Tail twitches']),
                        approaches=tobool(item['Approaches']),
                        indifferent=tobool(item['Indifferent']),
                        runs_from=tobool(item['Runs from']),
                        )
                    created.save()
           
                except FileNotFoundError:
                    raise CommandError("File {} does not exist".format(file_path))


