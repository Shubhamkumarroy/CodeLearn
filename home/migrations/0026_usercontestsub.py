# Generated by Django 4.2 on 2023-08-26 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_delete_usercontestsub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usercontestsub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('timetaken', models.CharField(max_length=50)),
                ('memorytaken', models.CharField(max_length=50)),
                ('verdict', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cproblem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cproblem')),
                ('newcontest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.newcontest')),
                ('user_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user_detail')),
            ],
        ),
    ]
