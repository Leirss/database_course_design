# Generated by Django 2.2.6 on 2019-12-04 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20191202_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Organizer',
            new_name='organizer',
        ),
    ]
