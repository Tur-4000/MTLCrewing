# Generated by Django 2.1.7 on 2019-03-22 08:01

import crewing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crewing', '0008_seamans_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seamans',
            name='foto',
            field=models.ImageField(null=True, upload_to=crewing.models.get_timestamp_path, verbose_name='Фото'),
        ),
    ]