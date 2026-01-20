from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    image = models.ImageField()
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.category}: {self.product_name}'

