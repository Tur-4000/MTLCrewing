from django.db import models

from crewing.models import Seamans, Ranks


class Ability360(models.Model):
    ability = models.CharField(max_length=32,
                               db_index=True,
                               blank=False,
                               verbose_name='Компетенция')
    # ranks = models.ManyToManyField(Ranks,
    #                                through='RankAbilityQuestion',
    #                                verbose_name='Должность',
    #                                related_name='abilities')

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'

    def __str__(self):
        return f'{self.ability}'


class Question360(models.Model):
    question = models.CharField(max_length=128,
                                db_index=True,
                                blank=False,
                                verbose_name='Вопрос')
    ranks = models.ManyToManyField(Ranks,
                                   # through='RankAbilityQuestion',
                                   verbose_name='Должность',
                                   related_name='questions')
    ability = models.ForeignKey(Ability360,
                                on_delete=models.CASCADE,
                                verbose_name='Компетенция',
                                related_name='questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['ability', 'question']

    def __str__(self):
        return f'{self.question}'


# class RankAbilityQuestion(models.Model):
#     rank = models.ForeignKey(Ranks, on_delete=models.CASCADE)
#     ability = models.ForeignKey(Ability360, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question360, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ['ability', 'question']


class Scoring360SeamanAbility(models.Model):
    date = models.DateTimeField(verbose_name='Метка времени',
                                db_index=True,
                                blank=False)
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Оцениваемый моряк',
                               db_index=True,
                               blank=False,
                               related_name='appraise_to')
    appraiser = models.ForeignKey(Seamans,
                                  on_delete=models.CASCADE,
                                  verbose_name='Кто оценивал',
                                  related_name='appraise_from')
    ability = models.ForeignKey(Ability360,
                                on_delete=models.CASCADE,
                                verbose_name='Компетенция')
    ability_value = models.DecimalField(verbose_name='Оценка',
                                        db_index=True,
                                        max_digits=2,
                                        decimal_places=1,
                                        blank=True,
                                        null=True,
                                        default=None)

    class Meta:
        verbose_name = 'Оценка 360'
        verbose_name_plural = 'Оценки 360'
        ordering = ['seaman', 'date']

    def __str__(self):
        return f'{self.seaman}: {self.date}'


class Scoring360AbilitySum(models.Model):
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Моряк',
                               blank=False)
    ability = models.ForeignKey(Ability360,
                                on_delete=models.CASCADE,
                                verbose_name='Компетенция')
    ability_value = models.DecimalField(db_index=True,
                                        max_digits=2,
                                        decimal_places=1,
                                        verbose_name='Оценка')

    class Meta:
        verbose_name = 'Суммарная оценка по компетенции'

    def __str__(self):
        return f'{self.seaman} - {self.ability}: {self.ability_value}'
