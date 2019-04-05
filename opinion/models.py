from datetime import datetime
from os.path import splitext

from django.db import models

from config.utils import gen_slug
from crewing.models import Seamans,Contracts


def get_opinionfile_path(instance, filename):

    return 'opinions/{}-{}{}'.format(gen_slug(splitext(filename)[0]),
                                     int(datetime.now().timestamp()),
                                     splitext(filename)[1])


class Opinion(models.Model):
    seaman = models.ForeignKey(Seamans,
                               on_delete=models.CASCADE,
                               verbose_name='Моряк')
    date = models.DateField(verbose_name='Дата отзыва')
    contract = models.ForeignKey(Contracts,
                                 on_delete=models.CASCADE,
                                 verbose_name='Контракт',
                                 blank=True,
                                 null=True,
                                 default=None)
    author = models.CharField(max_length=64,
                              db_index=True,
                              blank=False,
                              verbose_name='Автор отзыва')
    opinion_text = models.TextField(verbose_name='Отзыв')
    opinion_file = models.FileField(verbose_name='Файл',
                                    upload_to=get_opinionfile_path,
                                    blank=True,
                                    null=True,
                                    default=None)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-date']

    def __str__(self):
        return f'{self.author}: {self.opinion_text}'
