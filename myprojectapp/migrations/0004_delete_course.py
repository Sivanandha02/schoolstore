# Generated by Django 4.2.5 on 2023-11-04 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0003_rename_courses_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]