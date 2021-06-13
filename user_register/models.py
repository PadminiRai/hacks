from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Employee(models.Model):
    eno = models.IntegerField(max_length=10,primary_key=True)
    ename = models.CharField(max_length=20,null = False)
    mobile = models.IntegerField(max_length=10,null = False)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

class details(models.Model):
    uid = models.CharField(max_length=10,primary_key=True)
    pwd = models.CharField(max_length=20,null = False)
   
# Create your models here.
