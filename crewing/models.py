from django.db import models


class Seamans(models.Model):
    last_name = models.CharField(max_length=128,
                                 db_index=True,
                                 blank=False,
                                 verbose_name='Фамилия')
    first_name = models.CharField(max_length=128,
                                  db_index=True,
                                  blank=False,
                                  verbose_name='Имя')

    class Meta:
        verbose_name = 'Моряк'
        verbose_name_plural = 'Моряки'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
