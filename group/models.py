from django.db import models


class Group(models.Model):
    description = models.CharField(max_length=100)
    sauces = models.ManyToManyField('sauce.Sauce', blank=True)

    def __str__(self):
        return str(self.description)
