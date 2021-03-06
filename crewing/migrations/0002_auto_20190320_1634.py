# Generated by Django 2.1.7 on 2019-03-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seamans',
            old_name='first_name',
            new_name='first_name_en',
        ),
        migrations.RenameField(
            model_name='seamans',
            old_name='last_name',
            new_name='last_name_en',
        ),
        migrations.AddField(
            model_name='seamans',
            name='first_name_ru',
            field=models.CharField(db_index=True, default='Иванов', max_length=128, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seamans',
            name='first_name_ua',
            field=models.CharField(db_index=True, default='Иван', max_length=128, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seamans',
            name='last_name_ru',
            field=models.CharField(db_index=True, default='иванов', max_length=128, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seamans',
            name='last_name_ua',
            field=models.CharField(db_index=True, default='Иванов', max_length=128, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
