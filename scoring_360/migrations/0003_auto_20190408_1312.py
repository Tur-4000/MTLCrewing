# Generated by Django 2.1.7 on 2019-04-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_360', '0002_auto_20190408_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ability360',
            name='ranks',
        ),
        migrations.RemoveField(
            model_name='question360',
            name='ranks',
        ),
    ]
