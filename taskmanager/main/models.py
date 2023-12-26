from django.db import models


class Task(models.Model):
    title = models.CharField("Ім'я користувача",max_length=50)
    task = models.TextField('Коментар')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Коментар'
        verbose_name_plural = 'Коментарі'