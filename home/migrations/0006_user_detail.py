# Generated by Django 4.2 on 2023-08-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_discussitem_exploreitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_detail_name', models.CharField(max_length=20)),
                ('user_detail_email', models.CharField(max_length=20)),
                ('user_detail_password', models.CharField(max_length=20)),
            ],
        ),
    ]