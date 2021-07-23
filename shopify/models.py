from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/static/images/sample.jpg'
        return url
    # @property
    # def imageURL(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/static/images/placeholder.png"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    transaction_id = models.BigIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.id)
    def get_cart_total(self):
        ordereditems = self.ordereditem_set.all()
        total = sum([product.get_total for product in ordereditems])
        return total

    def get_cart_products(self):
        ordereditems = self.ordereditem_set.all()
        total = sum([product.quantity for product in ordereditems])
        return total

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.order)

    def get_total(self):
        total = self.product.price * self.quantity
        return total