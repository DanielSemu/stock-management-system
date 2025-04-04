from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField( max_length=50)

    def __str__(self):
        return self.name

class WareHouse(models.Model):
    name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name=models.CharField( max_length=50)
    phone_number=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StockItem(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    warehouse=models.ForeignKey(WareHouse, on_delete=models.CASCADE)
    min_stock_level=models.IntegerField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name