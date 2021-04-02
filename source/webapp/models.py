from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
category_choices = [('technical', 'техника'), ('product', 'продукты'), ('things', 'вещи')]


class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=100, null=False, blank=False, name='title')
    description = models.CharField(max_length=3000, null=True, blank=True, name='description')
    category = models.ForeignKey('webapp.Category', related_name="products", on_delete=models.PROTECT)
    reminder = models.IntegerField(validators=[MinValueValidator(0)], name='reminder')
    price = models.DecimalField(decimal_places=2, max_digits=7, name='price')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'


