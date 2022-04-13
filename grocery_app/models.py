from django.db import models

# Create your models here.
from django.db import models
class Grocery(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('users.User', related_name='grocery', on_delete=models.CASCADE)
    nowHave = models.IntegerField
    unitMeasure = models.CharField(max_length=200)
    eaten = models.IntegerField
    purchased: models.BooleanField
    img: models.ImageField(upload_to='images/', default='images/')
    
    def __str__(self):
        return self.name
