# Generated by Django 2.1.7 on 2019-04-08 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0027_auto_20190407_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ranks',
            options={'ordering': ['id', 'rank_title'], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
    ]