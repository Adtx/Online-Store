from django.contrib.auth.models import AbstractUser
from django.db import models

class Costumer(AbstractUser):
   telephone = models.CharField(max_length=30)
   street = models.CharField(max_length=30)
   city = models.CharField(max_length=30)
   district = models.CharField(max_length=30)
   zipcode = models.CharField(max_length=30)
   country = models.CharField(max_length=30)

   class Meta:
       db_table = 'costumers'

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ean = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    old_price = models.DecimalField(max_digits=8,decimal_places=2,blank=True,default=0.0)
    image = models.CharField(max_length=255,blank=True)
    is_on_sale = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    #categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        
    def __unicode__(self):
        return self.name

class Desktop(Product):
    d_processor = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)

    class Meta:
        db_table = 'desktops'

class SmartPhone(Product):
    os = models.CharField(max_length=255)
    s_processor = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    mobile_data = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)

    class Meta:
        db_table = 'smartphones'

class Processor(Product):
    base_freq = models.CharField(max_length=255)
    turbo_freq = models.CharField(max_length=255)
    num_cores = models.CharField(max_length=255)
    num_threads = models.CharField(max_length=255)
    tdp = models.CharField(max_length=255)
    cache = models.CharField(max_length=255)
    socket = models.CharField(max_length=255)

    class Meta:
        db_table = 'processors'

class Monitor(Product):
    size = models.CharField(max_length=255)
    aspect_ratio = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    response_time = models.CharField(max_length=255)
    conectivity = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)

    class Meta:
        db_table = 'monitors'

class Keyboard(Product):
    Layout = models.CharField(max_length=255)
    conectivity = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)

    class Meta:
        db_table = 'keyboards'
    
    def __unicode__(self):
        return self.name

class SSD(Product):
    Capacity = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    interface = models.CharField(max_length=255)
    seq_read_speed = models.CharField(max_length=255)
    seq_write_speed = models.CharField(max_length=255)
    random_read = models.CharField(max_length=255)
    random_write = models.CharField(max_length=255)

    class Meta:
        db_table = 'ssds'

class Router(Product):
    wireless_norm = models.CharField(max_length=255)
    segment = models.CharField(max_length=255)
    data_rate = models.CharField(max_length=255)
    antena = models.CharField(max_length=255)
    segnal_freq = models.CharField(max_length=255)
    ports = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)

    class Meta:
        db_table = 'routers'