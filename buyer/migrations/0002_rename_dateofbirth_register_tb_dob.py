# Generated by Django 4.1 on 2022-11-07 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_tb',
            old_name='dateofbirth',
            new_name='dob',
        ),
    ]
