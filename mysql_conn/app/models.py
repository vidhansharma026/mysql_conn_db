from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    deptno = models.IntegerField()
    salary = models.FloatField(max_length=200)
    job = models.CharField(max_length=200)
