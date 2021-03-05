from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
category_choices = [('technical', 'техника'), ('product', 'продукты'), ('things', 'вещи')]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, name='title')
    description = models.CharField(max_length=3000, null=True, blank=True, name='description')
    category = models.CharField(max_length=200, null=True, blank=True, choices=category_choices, name='category')
    reminder = models.IntegerField(validators=[MinValueValidator(0)], name='reminder')
    price = models.DecimalField(decimal_places=2, max_digits=7, name='price')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'
