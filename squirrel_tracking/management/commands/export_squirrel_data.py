from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from squdata.models import Squirreldata
from django.apps import apps


