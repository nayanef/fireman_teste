from django.db import models

# Create your models here.


class Quote(models.Model):
    text = models.CharField(max_length=700)
    author = models.CharField(max_length=100)
    
