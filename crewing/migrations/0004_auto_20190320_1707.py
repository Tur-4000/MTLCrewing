# Generated by Django 2.1.7 on 2019-03-20 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0003_auto_20190320_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in_date', models.DateField(verbose_name='Дата начала')),
                ('sign_off_date', models.DateField(verbose_name='Дата списания')),
            ],
            options={
                'verbose_name': 'Контракт',
                'verbose_name_plural': 'Контракты',
            },
        ),
        migrations.CreateModel(
            name='Opinions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата отзыва')),
                ('author', models.CharField(db_index=True, max_length=64, verbose_name='Автор отзыва')),
                ('opinion_text', models.TextField(verbose_name='Отзыв')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Contracts', verbose_name='Контракт')),
                ('seaman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Seamans', verbose_name='Моряк')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_title', models.CharField(db_index=True, max_length=64, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Vessels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(db_index=True, max_length=128, verbose_name='Название судна')),
                ('vessel_type', models.CharField(db_index=True, max_length=128, verbose_name='Тип судна')),
                ('dwt', models.IntegerField(db_index=True, verbose_name='Водоизмещение')),
            ],
            options={
                'verbose_name': 'Судно',
                'verbose_name_plural': 'Суда',
            },
        ),
        migrations.AddField(
            model_name='contracts',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crewing.Ranks', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='contracts',
            name='seaman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crewing.Seamans', verbose_name='Моряк'),
        ),
        migrations.AddField(
            model_name='contracts',
            name='vessel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crewing.Vessels', verbose_name='Судно'),
        ),
    ]
