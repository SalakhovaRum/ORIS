from django.db import models


class Orders(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Марка'
    )
    thing = models.CharField(
        max_length=120,
        verbose_name='Какая'
    )
    count = models.IntegerField(
        verbose_name='Количество',
        default=1,
    )

    def __str__(self):
        return f'Name:{self.name} {self.thing}'

# Create your models here.
