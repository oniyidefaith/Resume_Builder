# Generated by Django 4.1.3 on 2022-12-16 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='owner',
            new_name='own',
        ),
        migrations.RemoveField(
            model_name='links',
            name='Title',
        ),
    ]