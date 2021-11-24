from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length= 100, null=False, blank=False)
    def __str__(self):
        return self.name