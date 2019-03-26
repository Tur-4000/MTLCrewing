from datetime import datetime
from os.path import splitext

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_timestamp_path(instance, filename):
    return '{}{}'.format(datetime.now().timestamp(), splitext(filename)[1])


class Ranks(models.Model):
    rank_title = models.CharField(max_length=64,
                                  db_index=True,
                                  blank=False,
                                  verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

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


class Opinions(models.Model):
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Моряк')
    date = models.DateField(verbose_name='Дата отзыва')
    contract = models.ForeignKey(Contracts,
                                 on_delete=models.CASCADE,
                                 verbose_name='Контракт')
    author = models.CharField(max_length=64,
                              db_index=True,
                              blank=False,
                              verbose_name='Автор отзыва')
    opinion_text = models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-date']

    def __str__(self):
        return f'{self.author}: {self.opinion_text}'


class Seaman360Ability(models.Model):
    ability = models.CharField(max_length=32,
                               db_index=True,
                               blank=False,
                               verbose_name='Компетенция')
    ranks = models.ManyToManyField(Ranks, related_name='abilities')

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'

    def __str__(self):
        return f'{self.ability}'


class Seaman360Question(models.Model):
    # ABILITIES = (
    #     (1, 'Организаторские способности'),
    #     (2, 'Дисциплинированность'),
    #     (3, 'Старательность'),
    #     (4, 'Работа в команде'),
    #     (5, 'Работоспособность'),
    #     (6, 'Ответственность'),
    #     (7, 'Стрессоустойчивость'),
    #     (8, 'Лидерство'),
    #     (9, 'Уверенность в себе'),
    #     (10, 'Трудолюбие'),
    # )
    question = models.CharField(max_length=128,
                                db_index=True,
                                blank=False,
                                verbose_name='Вопрос')
    rank = models.ManyToManyField(Ranks,
                                  verbose_name='Должность',
                                  related_name='Компетенции')
    # ability = models.PositiveSmallIntegerField(choices=ABILITIES,
    #                                            db_index=True,
    #                                            blank=False,
    #                                            verbose_name='Компетенция')
    ability = models.ForeignKey(Seaman360Ability,
                                on_delete=models.CASCADE,
                                verbose_name='Компетенция')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['ability', 'question']

    def __str__(self):
        return f'{self.question}'


class Seaman360Rating(models.Model):
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Оцениваемый моряк',
                               db_index=True,
                               blank=False,
                               related_name='rates_to')
    date = models.DateTimeField(verbose_name='Метка времени',
                                db_index=True,
                                blank=False)
    appraiser = models.ForeignKey(Seamans,
                                  on_delete=models.CASCADE,
                                  verbose_name='Кто оценивал',
                                  related_name='rates_from')
    ability1 = models.DecimalField(verbose_name='Организаторские способности',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability2 = models.DecimalField(verbose_name='Дисциплинированность',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability3 = models.DecimalField(verbose_name='Старательность',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability4 = models.DecimalField(verbose_name='Работа в команде',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability5 = models.DecimalField(verbose_name='Работоспособность',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability6 = models.DecimalField(verbose_name='Ответственность',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability7 = models.DecimalField(verbose_name='Стрессоустойчивость',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability8 = models.DecimalField(verbose_name='Лидерство',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability9 = models.DecimalField(verbose_name='Уверенность в себе',
                                   db_index=True,
                                   max_digits=2,
                                   decimal_places=1)
    ability10 = models.DecimalField(verbose_name='Трудолюбие',
                                    db_index=True,
                                    max_digits=2,
                                    decimal_places=1)

    class Meta:
        verbose_name = 'Рейтинг 360 (моряки)'
        verbose_name_plural = 'Рейтинги 360 (моряки)'

    def __str__(self):
        return f'{self.seaman}: {self.date}'
