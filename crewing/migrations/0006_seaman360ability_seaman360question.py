# Generated by Django 2.1.7 on 2019-03-21 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0005_auto_20190321_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seaman360Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.CharField(db_index=True, max_length=32, verbose_name='Компетенция')),
            ],
            options={
                'verbose_name': 'Компетенция',
                'verbose_name_plural': 'Компетенции',
            },
        ),
        migrations.CreateModel(
            name='Seaman360Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(db_index=True, max_length=128, verbose_name='Вопрос')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Seaman360Ability', verbose_name='Компетенция')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Ranks', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
