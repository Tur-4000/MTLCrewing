# Generated by Django 2.1.7 on 2019-04-08 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0031_auto_20190408_1553'),
        ('scoring_360', '0004_auto_20190408_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankAbilityQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring_360.Ability360')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring_360.Question360')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Ranks')),
            ],
        ),
        migrations.AddField(
            model_name='ability360',
            name='ranks',
            field=models.ManyToManyField(related_name='abilities', through='scoring_360.RankAbilityQuestion', to='crewing.Ranks', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='question360',
            name='ranks',
            field=models.ManyToManyField(related_name='questions', through='scoring_360.RankAbilityQuestion', to='crewing.Ranks', verbose_name='Должность'),
        ),
        migrations.AlterUniqueTogether(
            name='rankabilityquestion',
            unique_together={('ability', 'question')},
        ),
    ]
