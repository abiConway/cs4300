from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description', max_length=200)
    release_date = models.DateField('Release Date', auto_now=False, auto_now_add=False, null=True, blank=True)
    duration = models.PositiveIntegerField('Duration', help_text="Duration in minutes")

        #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title





class Seat(models.Model):
    seat_number = models.CharField('Seat Number', max_length=10, unique=True)
    is_booked = models.BooleanField('Booked', default=False)

    def __str__(self):
        return f"Seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    booking_date = models.DateTimeField('Booking Date', auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"


