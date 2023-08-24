# Generated by Django 4.2 on 2023-08-23 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_cproblem_pdate_alter_newcontest_ndate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitinput_data', models.TextField()),
                ('submitexpected_output', models.TextField()),
                ('cproblem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cproblem')),
            ],
        ),
    ]
