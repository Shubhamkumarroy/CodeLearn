# Generated by Django 4.2 on 2023-08-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_contest_admin_cadmin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadmin',
            name='Cauthor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadmin',
            name='Cname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cproblem',
            name='compexity',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cproblem',
            name='constraints',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cproblem',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='newcontest',
            name='nauthor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='newcontest',
            name='nname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_detail_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_detail_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='user_detail_password',
            field=models.CharField(max_length=100),
        ),
    ]
