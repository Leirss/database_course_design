# Generated by Django 2.2.6 on 2019-12-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20191202_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='content',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='award',
            name='style',
            field=models.CharField(max_length=200),
        ),
    ]
