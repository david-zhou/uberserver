from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
        

class User(models.Model):
    email = models.EmailField(max_length = 50, primary_key = True)
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    country = models.CharField(max_length = 50)
    home = models.CharField(max_length = 50, blank = True)
    home_lat = models.CharField(max_length = 20, blank = True)
    home_long = models.CharField(max_length = 20, blank = True)
    work = models.CharField(max_length = 50, blank = True)
    work_lat = models.CharField(max_length = 20, blank = True)
    work_long = models.CharField(max_length = 20, blank = True)
    
class Driver(models.Model):
    driver_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    vehicle = models.CharField(max_length = 50)
    available = models.BooleanField(default = True)
    pos_lat = models.FloatField(blank = True)
    pos_long = models.FloatField(blank = True)
    gcm_id = models.CharField(max_length = 200, blank = True)
    license_plate = models.CharField(max_length = 10, blank = True)
    
class Credit_Card(models.Model):
    credit_card_number = models.CharField(primary_key = True, max_length = 20)
    email = models.ForeignKey(User)
    mm = models.CharField(max_length = 2)
    yy = models.CharField(max_length = 2)
    cvv = models.CharField(max_length = 3)
    postal_code = models.CharField(max_length = 5, blank = True)
    mail = models.BooleanField(default = False)
    
class User_Ride(models.Model):
    ride_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User)
    driver_id = models.ForeignKey(Driver)
    credit_card_number = models.ForeignKey(Credit_Card)
    date = models.DateTimeField(null = True)
    initial_pos = models.CharField(max_length = 50, blank = True)
    initial_lat = models.FloatField(null = True)
    initial_long = models.FloatField(null = True)
    final_pos = models.CharField(max_length = 50, blank = True)
    final_lat = models.FloatField(null = True)
    final_long = models.FloatField(null = True)
    distance = models.DecimalField(max_digits = 5, decimal_places = 1, null = True)
    time = models.CharField(max_length = 10, blank = True)
    fee = models.IntegerField(null = True)
    final_fee = models.IntegerField(null = True)
    user_rating = models.IntegerField(null = True)
    driver_rating = models.IntegerField(null = True)
    pending_ride_id = models.IntegerField(null = True)
    
class Pending_Ride(models.Model):
    pending_ride_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User)
    user_lat = models.FloatField(null = True)
    user_lon = models.FloatField(null = True)
    user_destination_lat = models.FloatField(null = True)
    user_destination_lon = models.FloatField(null = True)
    