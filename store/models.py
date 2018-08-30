from django.contrib.auth.models import AbstractUser
from django.db import models
import decimal

class Costumer(AbstractUser):
   telephone = models.CharField(max_length=30,blank=True)
   street = models.CharField(max_length=30,blank=True)
   city = models.CharField(max_length=30,blank=True)
   district = models.CharField(max_length=30,blank=True)
   zipcode = models.CharField(max_length=30,blank=True)
   country = models.CharField(max_length=30,blank=True)

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
    brand = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
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

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, unique=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, unique=False, null=True)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']
    
    def total(self):
        return self.quantity * self.product.price
    
    def name(self):
        return self.product.name
    
    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8,decimal_places=2, null=True)
    costumer = models.ForeignKey('Costumer', on_delete=models.PROTECT, unique=False)

    class Meta:
        db_table = 'orders'
        ordering = ['date']

    # def get_items(self):
    #     items = CartItem.objects.filter(order=self)
    #     return items

    def total(self):
        total = decimal.Decimal('0.00')
        items = self.cartitem_set.all()
        for item in items:
            total += item.total()
        return total