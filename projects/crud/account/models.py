from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    
class Categories(models.Model):
    categories = models.CharField(max_length=100)


# class CategoriesImg(models.Model):
#     categories = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True)
#     image = models.ImageField(upload_to='images/')



class EmployeeDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
