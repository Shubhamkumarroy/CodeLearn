# Generated by Django 4.2 on 2023-08-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_usercontestsub'),
    ]

    operations = [
        migrations.AddField(
            model_name='myubmission',
            name='output',
            field=models.TextField(default='shubham'),
        ),
        migrations.AddField(
            model_name='usercontestsub',
            name='output',
            field=models.TextField(default='shubham'),
        ),
    ]