from django.db import models
from datetime import datetime, date
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    descrip = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)

    def __str__(self):
        return self.title