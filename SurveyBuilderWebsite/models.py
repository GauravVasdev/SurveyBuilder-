# Create your models here.
from django.db import models
class serverconnection(models.Model):
    PersonID=models.CharField(max_length=255)
    Nameofsurvey=models.CharField(max_length=255)
    FormContent=models.CharField(max_length=255)
    Formattrndvalues=models.CharField(max_length=255)

class responsemodel(models.Model):
        PersonID=models.IntegerField()
        Formid=models.IntegerField()
        Nameofsurvey=models.CharField(max_length=255)
        Formattrndvalues=models.CharField(max_length=255)

class registeration(models.Model):
    Position=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
