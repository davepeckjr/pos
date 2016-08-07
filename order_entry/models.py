from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.name)

class MenuItem(models.Model):
    build = models.ManyToManyField(Ingredients)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

class YouPickTwo(models.Model):
    pick1 = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    pick2 = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    side = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
