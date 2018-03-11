from django.db import models

# Create your models here.
class Student(models.Model):
   fname=models.CharField(max_length=15)
   lname=models.CharField(max_length=15)
   age=models.IntegerField(default=15)
   dn=models.DateTimeField()
   def __str__(self):
      return self.fname

class Degree(models.Model):
   sid=models.ForeignKey(Student,on_delete=models.CASCADE)
   degree = models.IntegerField(default=15)
   def __str__(self):
      return self.sid.fname


