# Generated by Django 4.2 on 2023-08-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_cupdatetestcase_cupdatesolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='cproblem',
            name='pdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newcontest',
            name='ndate',
            field=models.DateTimeField(),
        ),
    ]