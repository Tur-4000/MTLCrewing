# Generated by Django 2.1.7 on 2019-04-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0023_auto_20190327_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinions',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crewing.Contracts', verbose_name='Контракт'),
        ),
    ]