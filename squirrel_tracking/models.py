from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Sighting(models.Model):
    Latitude = models.FloatField(
            help_text =_('Latitude of sighting'),
            )
    Longitude = models.FloatField(
            help_text = _('Longitude of sighting'),
            )
    Unique_Squirrel_ID = models.CharField(
            max_length =100,
            unique=True,
            help_text = _('Unique id of squirrel'),
        )
    MORN = 'AM'
    AFTER ='PM'
    SHIFT_CHOICE = [
            (MORN, _('AM')),
            (AFTER, _('PM')),
            ]
    Shift = models.CharField(
            max_length = 10,
            help_text = _('Shift of sighting'),
            choices = SHIFT_CHOICE,
            default = MORN,
            )
    Date = models.DateField(
            help_text = _('Date of this sighting'),
            )
    Age = models.CharField(
            max_length = 100,
            blank = True,
            help_text = _('Age of this squirrel'),
            )
    Primary_Fur_color = models.CharField(
           blank =True,
           max_length = 50,
           )
    Location = models.TextField(
            blank = True,
            )
    Specific_Location = models.TextField(
            blank = True,
            )
    Running = models.BooleanField(
            blank = True,
            )
    Chasing = models.BooleanField(
            blank = True,
            )
    Climbing = models.BooleanField(
            blank = True,
            )
    Eating = models.BooleanField(
            blank = True,
            )
    Foraging = models.BooleanField(
            blank = True,
            )
    Other_Activities = models.TextField(
            max_length = 100,
            blank = True,
            )
    Kuks = models.BooleanField(
            blank = True,
            )
    Quaas = models.BooleanField(
            blank = True,
            )
    Moans = models.BooleanField(
            blank = True,
            )
    Tail_flags =models.BooleanField(
            blank = True,
            )
    Tail_twitches = models.BooleanField(
            blank = True,
            )
    Approaches = models.BooleanField(
            blank = True,
            )
    Indifferent = models.BooleanField(
            blank = True,
            )
    Runs_from = models.BooleanField(
            blank = True,
            )
    def __str__(self):
        return self.Unique_Squirrel_ID


