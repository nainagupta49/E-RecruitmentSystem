from django.db import models

class candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, default='M')
    phone = models.CharField(max_length=12, default='0000000000')
     
    