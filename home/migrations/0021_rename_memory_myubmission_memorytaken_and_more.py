# Generated by Django 4.2 on 2023-08-25 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_myubmission_verdict'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myubmission',
            old_name='memory',
            new_name='memorytaken',
        ),
        migrations.RenameField(
            model_name='myubmission',
            old_name='time',
            new_name='timetaken',
        ),
    ]
