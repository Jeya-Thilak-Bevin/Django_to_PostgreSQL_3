from django.db import models

# Create your models here.
class Company(models.Model):
    code=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    date=models.DateField()
    price=models.FloatField()
    volume=models.IntegerField()
    def __str__(self):
        return self.code
