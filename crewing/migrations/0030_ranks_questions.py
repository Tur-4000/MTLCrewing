# Generated by Django 2.1.7 on 2019-04-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_360', '0004_auto_20190408_1319'),
        ('crewing', '0029_ranks_abilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranks',
            name='questions',
            field=models.ManyToManyField(related_name='ranks', to='scoring_360.Question360', verbose_name='Вопросы'),
        ),
    ]
