from django.db import models
from django.core.validators import MinValueValidator



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


class Basket(BaseModel):
    product = models.ForeignKey(Product, null=True, related_name="basket",
                                on_delete=models.CASCADE)

    total = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='total')


class Order(BaseModel):
    product_order = models.ManyToManyField(max_length=100, null=False, blank=False, name='product_order')
    name = models.CharField(max_length=100, null=False, blank=False, name='name')
    number = models.IntegerField(validators=[MinValueValidator(0)], name='number')
    adress = models.CharField(max_length=100, null=False, blank=False, name='adress')