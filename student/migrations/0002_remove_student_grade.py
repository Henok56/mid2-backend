# Generated by Django 4.1.4 on 2023-01-01 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
    ]
