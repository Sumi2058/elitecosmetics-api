from django.db import models 


class EliteUser(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)


    
    