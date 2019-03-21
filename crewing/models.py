from django.db import models


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
                                    blank=False,
                                    verbose_name='Фамилия (UA)')
    first_name_ua = models.CharField(max_length=128,
                                     db_index=True,
                                     blank=False,
                                     verbose_name='Имя (UA)')

    class Meta:
        verbose_name = 'Моряк'
        verbose_name_plural = 'Моряки'

    def __str__(self):
        return f'{self.last_name_ru} {self.first_name_ru}'


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
    sign_off_date = models.DateField(verbose_name='Дата списания')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'

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
