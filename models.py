from django.db import models

# Create your models here.

class Booking(models.Model):
    
    BIKE_TYPE = (
        ('RB', 'ROAD BIKE'
         'SB', 'SPORT BIKE'
         'EL', 'ELECTRICAL BIKE'
         'MB', 'MOUNTAIN BIKE')
        
    )
    



    booking_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    booking_date=models.DateTimeField(auto_now_add=True)
    bike_type=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Boys(models.Model):
    rno= models.IntegerField(primary_key=True)
    marks=models.IntegerField()
    
    class Meta:
        db_table="boys"
        
class Info(models.Model):
    rno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    marks=models.IntegerField() 
    
    class Meta:
        db_table="information"
        
        
        
class User(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=45, blank=True, null=True)
    mobno = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    imagepath = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        

    
    

