# Generated by Django 5.0 on 2023-12-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=1024)),
                ('start_date', models.DateTimeField(verbose_name='Startdatum')),
                ('end_date', models.DateTimeField(verbose_name='Enddatum')),
                ('tn_count', models.IntegerField(default=0, help_text='TN Anzahl')),
            ],
        ),
    ]
