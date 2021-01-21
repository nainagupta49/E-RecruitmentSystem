from django.db import models

class Jobs(models.Model):
    description = models.TextField()
    image = models.FileField(upload_to='images/',blank=True, null=True)