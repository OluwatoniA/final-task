from django.db import models

# Create your models here.
class Record(models.Model):
    id = models.AutoField(max_length=50, primary_key=True)
    room_number = models.IntegerField(max_length=50)
    amount_paid = models.IntegerField(max_length=1000000)
    occupant_name = models.CharField(max_length=100)
    occupant_email = models.EmailField(max_length=50)
    occupant_occupation = models.CharField(max_length=100)
    number_of_night = models.IntegerField(max_length=50)
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.occupant_name + " " + str(self.room_number)