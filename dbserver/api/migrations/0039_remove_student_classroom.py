# Generated by Django 2.2.6 on 2019-12-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20191206_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
    ]
