from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, blank=True) 
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%y/%m')
    caategory = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


