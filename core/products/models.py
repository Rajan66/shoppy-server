from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    imageUrl = models.ImageField(
        upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    imageUrl = models.ImageField(upload_to='category_images/')
    gender = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return f"Cart {self.id} for User {self.user_id}"
