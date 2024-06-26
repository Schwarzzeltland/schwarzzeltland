# Generated by Django 5.0 on 2024-05-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_trip_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Haus'), (1, 'Pfadfinderzeltplatz'), (2, 'Campingplatz'), (3, 'Freier Platz')], help_text='Typ des Events', null=True)),
                ('description', models.CharField(blank=True, default='', max_length=1024)),
                ('latitude', models.FloatField(default=0.0, help_text='Latitude')),
                ('longitude', models.FloatField(default=0.0, help_text='Longitude')),
            ],
        ),
    ]
