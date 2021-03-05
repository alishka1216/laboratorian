from django.db import models

# Create your models here.
category_choices = [('technical', 'техника'), ('product', 'продукты'), ('things', 'вещи')]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=3000, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True, choices=category_choices)
    price.ost = models.IntegerField(min_value=0)
    price = models.DecimalField()