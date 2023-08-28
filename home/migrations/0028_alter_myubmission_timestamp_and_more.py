# Generated by Django 4.2.4 on 2023-08-28 15:53

from django.db import migrations
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_myubmission_output_usercontestsub_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myubmission',
            name='timestamp',
            field=home.models.IndianDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usercontestsub',
            name='timestamp',
            field=home.models.IndianDateTimeField(default=django.utils.timezone.now),
        ),
    ]
