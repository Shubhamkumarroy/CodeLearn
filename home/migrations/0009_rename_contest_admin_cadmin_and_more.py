# Generated by Django 4.2 on 2023-08-22 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_newcontest_contest_testcase_contest_solution_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contest_admin',
            new_name='Cadmin',
        ),
        migrations.RenameModel(
            old_name='Contest_problem',
            new_name='Cproblem',
        ),
        migrations.RenameModel(
            old_name='Contest_Solution',
            new_name='CSolution',
        ),
        migrations.RenameModel(
            old_name='Contest_testCase',
            new_name='CtestCase',
        ),
        migrations.RenameField(
            model_name='cadmin',
            old_name='contest_author',
            new_name='Cauthor',
        ),
        migrations.RenameField(
            model_name='cadmin',
            old_name='contest_date',
            new_name='Cdate',
        ),
        migrations.RenameField(
            model_name='cadmin',
            old_name='contest_name',
            new_name='Cname',
        ),
        migrations.RenameField(
            model_name='newcontest',
            old_name='newcontest_author',
            new_name='nauthor',
        ),
        migrations.RenameField(
            model_name='newcontest',
            old_name='newcontest_date',
            new_name='ndate',
        ),
        migrations.RenameField(
            model_name='newcontest',
            old_name='newcontest_name',
            new_name='nname',
        ),
    ]
