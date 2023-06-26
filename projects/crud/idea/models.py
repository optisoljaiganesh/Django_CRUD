from django.db import models

# Create your models here.


class TestModel:
    name: str
    age: int    
    address: str
    phone: int
    active: bool

class IdeaModel(models.Model):
    name = models.CharField(max_length=200)
    age= models.IntegerField()
    address= models.CharField(max_length=500)
    phone= models.IntegerField()
    active= models.BooleanField(default=True)
