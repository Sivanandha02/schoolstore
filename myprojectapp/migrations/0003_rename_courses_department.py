# Generated by Django 4.2.5 on 2023-11-04 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0002_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Department',
        ),
    ]