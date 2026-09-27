from django.db import models

class Emp(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    department=models.CharField(max_length=20)
    working=models.BooleanField(default=True)