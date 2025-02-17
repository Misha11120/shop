from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="brands", null=True, blank=True)
    description = models.TextField(max_length=500,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "categories"



class Shoe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500,null=True, blank=True)
    color = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=3, decimal_places=1)
    sale = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="shoes")
    gender = models.CharField(max_length=6, choices=(("female","Female"),("male","Male")))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shoes")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="shoes")
    image = models.ImageField(upload_to="brands", null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.name}-{self.brand}"

    

