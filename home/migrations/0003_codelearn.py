# Generated by Django 4.2 on 2023-08-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_problem_tag_testcase_solution_problem_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='codelearn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
