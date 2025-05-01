from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Represents a product category in the e-commerce store.
    
    Attributes:
        name (CharField): The name of the category (max_length=100, unique)
        slug (SlugField): URL-friendly version of the name (max_length=100, unique)
    
    Meta:
        verbose_name_plural (str): The plural name for the model in the admin interface
    
    Methods:
        __str__(): Returns the category name
        get_absolute_url(): Returns the URL for the category detail page
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:category_detail', args=[self.slug])

class Product(models.Model):
    """
    Represents a product item in the e-commerce store.
    
    Attributes:
        category (ForeignKey): Reference to the Category model
        name (CharField): Name of the product (max_length=100)
        slug (SlugField): URL-friendly version of the name (max_length=100)
        image (ImageField): Product image (uploaded to 'products/' directory)
        description (TextField): Detailed product description
        price (DecimalField): Product price (max_digits=10, decimal_places=2)
        available (BooleanField): Product availability status
        created (DateTimeField): Product creation timestamp
        updated (DateTimeField): Last update timestamp
    
    Meta:
        ordering (tuple): Default ordering by product name
    
    Methods:
        __str__(): Returns the product name
        get_absolute_url(): Returns the URL for the product detail page
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

# Create your models here.
