from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
  created = models.DateTimeField(auto_now_add= True)
  name = models.CharField(max_length=100, blank=True, default="")
  price = models.DecimalField(max_digits=20, decimal_places=2)
  description = models.TextField(max_length=300, default='')
  quantity = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, default="")


  class Meta:
    ordering =('name',)

