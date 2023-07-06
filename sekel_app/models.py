from django.db import models

class Category(models.Model):
    cate_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cate_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
