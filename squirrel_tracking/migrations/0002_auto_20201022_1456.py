# Generated by Django 3.1.2 on 2020-10-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='Primary_Fur_color',
        ),
        migrations.AddField(
            model_name='sighting',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Date',
            field=models.DateField(help_text='format is yyyy-mm-dd'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=10),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='Unique_Squirrel_ID',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
