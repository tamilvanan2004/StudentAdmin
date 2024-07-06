from django.db import models





class Mentor(models.Model):
    Name=models.CharField(max_length=30)
    Mentor=models.CharField(max_length=30)
    



class Students(models.Model):
    mentor =models.CharField(max_length=50,null=True,blank=True)
    Name = models.CharField(max_length=30)
    Course = models.CharField(max_length=30)
    Confirm = models.CharField(max_length=30)
    Bcode = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    TimeSlot =  models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    
    