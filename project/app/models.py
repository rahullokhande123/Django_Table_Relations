from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar=models.IntegerField(primary_key=50)
    def __str__(self):
        return str(self.aadhar)
    
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_des=models.TextField()
    
    def __str__(self):
        return str(self.dep_name)

