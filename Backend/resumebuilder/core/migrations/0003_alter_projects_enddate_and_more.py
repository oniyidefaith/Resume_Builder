# Generated by Django 4.1.3 on 2022-12-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_profile_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='EndDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='volunteerexperience',
            name='EndDate',
            field=models.DateField(blank=True),
        ),
    ]