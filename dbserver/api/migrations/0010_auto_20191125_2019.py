# Generated by Django 2.2.6 on 2019-11-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191125_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
