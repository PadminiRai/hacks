from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class evnts(models.Model):
    edate = models.CharField(max_length=20)
    etime = models.CharField(max_length=20)
    eloct = models.CharField(max_length=50)

class details(models.Model):
    uid = models.CharField(max_length=10,primary_key=True)
    email = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    utype = models.CharField(max_length=2)
   
# Create your models here.
