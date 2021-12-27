from django.db import models
from django.conf import settings


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date = models.DateField()

    def __str__(self) :
        return self.name

class Room(models.Model):
    Room_categeris = {
        ('WAC','AC'),
        ('NAC', 'NON AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QU','QUEEN')
    }
    number = models.IntegerField()  
    category=models.CharField(max_length=3, choices=Room_categeris)
    bed = models.IntegerField()     
    capacity = models.IntegerField()  
    def __str__(self):
        return f'{self.number}.{self.category} with {self.bed} for {self.capacity} people'

class Booking(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

