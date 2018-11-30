from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
# listings
# id: int
# title: str 
# address: str 
# city: str 
# state: str 
# zipcode: str 
# description: text 
# price: int
# bedroos: int
# bathrooms: int
# garage: int [0]
# sqft: int
# lot_size: float
# is_published: bool [true]
# list_date: date
# photo_main: str
# photo_1: str
# photo_2: str
# photo_3: str
# photo_4: str
# photo_5: str
# photo_6: str

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedroos = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title