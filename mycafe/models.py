from django.db import models

class MenuItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.ManyToManyField('category',related_name='item')

    def __str__(self):
        return self.name
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    items = models.ManyToManyField('MenuItems',related_name='order',blank=True)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

# Create your models here.
