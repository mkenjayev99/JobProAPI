# Generated by Django 4.2 on 2023-05-13 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_remove_applyjob_created_date_applyjob_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='types',
        ),
        migrations.RemoveField(
            model_name='job',
            name='working_day',
        ),
    ]
