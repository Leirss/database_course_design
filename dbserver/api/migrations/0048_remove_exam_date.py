# Generated by Django 2.2.6 on 2019-12-15 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_exam_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='date',
        ),
    ]
