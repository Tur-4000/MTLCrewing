from datetime import datetime
from os.path import splitext

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_timestamp_path(instance, filename):
    return '{}{}'.format(datetime.now().timestamp(), splitext(filename)[1])


# TODO: после перестройки миграций удалить
def get_opinionfile_path(instance, filename):
    return 'opinions/{}-{}{}'.format(splitext(filename)[0],
                                     int(datetime.now().timestamp()),
                                     splitext(filename)[1])


class Ranks(models.Model):
    rank_title = models.CharField(max_length=64,
                                  db_index=True,
                                  blank=False,
                                  verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['id', 'rank_title']

    def __str__(self):
        return f'{self.rank_title}'


class Seamans(models.Model):
    last_name_en = models.CharField(max_length=128,
                                    db_index=True,
                                    blank=False,
                                    verbose_name='Фамилия (EN)')
    first_name_en = models.CharField(max_length=128,
                                     db_index=True,
                                     blank=False,
                                     verbose_name='Имя (EN)')
    last_name_ru = models.CharField(max_length=128,
                                    db_index=True,
                                    blank=False,
                                    verbose_name='Фамилия (RU)')
    first_name_ru = models.CharField(max_length=128,
                                     db_index=True,
                                     blank=False,
                                     verbose_name='Имя (RU)')
    last_name_ua = models.CharField(max_length=128,
                                    db_index=True,
                                    blank=True,
                                    null=True,
                                    verbose_name='Фамилия (UA)')
    first_name_ua = models.CharField(max_length=128,
                                     db_index=True,
                                     blank=True,
                                     null=True,
                                     verbose_name='Имя (UA)')
    foto = models.ImageField(verbose_name='Фото',
                             upload_to=get_timestamp_path,
                             null=True,
                             default='seaman.png')
    last_rank = models.ForeignKey(Ranks,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Последняя должность',
                                  blank=True,
                                  null=True)

    class Meta:
        verbose_name = 'Моряк'
        verbose_name_plural = 'Моряки'

    def __str__(self):
        return f'{self.last_name_ru} {self.first_name_ru}'


class Vessels(models.Model):
    vessel_name = models.CharField(max_length=128,
                                   db_index=True,
                                   blank=False,
                                   verbose_name='Название судна')
    vessel_type = models.CharField(max_length=128,
                                   db_index=True,
                                   blank=False,
                                   verbose_name='Тип судна')
    dwt = models.IntegerField(db_index=True,
                              blank=False,
                              verbose_name='Водоизмещение')

    class Meta:
        verbose_name = 'Судно'
        verbose_name_plural = 'Суда'

    def __str__(self):
        return f'{self.vessel_name}'


class Contracts(models.Model):
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Моряк')
    rank = models.ForeignKey(Ranks,
                             on_delete=models.DO_NOTHING,
                             verbose_name='Должность')
    vessel = models.ForeignKey(Vessels,
                               on_delete=models.DO_NOTHING,
                               verbose_name='Судно')
    sign_in_date = models.DateField(verbose_name='Дата начала')
    sign_off_date = models.DateField(verbose_name='Дата списания',
                                     blank=True,
                                     null=True)

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
        ordering = ['-sign_in_date']

    def __str__(self):
        return f'{self.vessel} {self.sign_in_date}/{self.sign_off_date}'
