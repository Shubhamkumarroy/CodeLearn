# Generated by Django 4.2 on 2023-08-26 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_memory_myubmission_memorytaken_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myubmission',
            name='newcontest',
            field=models.ForeignKey(default=43, on_delete=django.db.models.deletion.CASCADE, to='home.newcontest'),
            preserve_default=False,
        ),
    ]
