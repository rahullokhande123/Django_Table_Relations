from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar=models.IntegerField(primary_key=50)
    def __str__(self):
        return str(self.aadhar)
    
