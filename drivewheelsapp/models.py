from django.db import models


# Create your models here.

class Car(models.Model):
    FUEL_TYPE_CHOICES = ((1, 'Petrol'),(2, 'Diesel'),(3, 'CNG'))
    TRANS_TYPE_CHOICES = ((4, 'Manual'),(5, 'Automatic'))
    SEATS_TYPE_CHOICES = ((6, '5STR'),(7, '7STR'))
    LOCATION_CHOICES=((8, 'pune'),(9, 'mumbai'),(10, 'hyderabad'),(11, 'chiplun'),(12, 'ratnagiri'))
    
    
    carname=models.CharField(max_length=300)
    fuel=models.IntegerField(choices=FUEL_TYPE_CHOICES)
    transmission=models.IntegerField(choices=TRANS_TYPE_CHOICES )
    seats=models.IntegerField(choices=SEATS_TYPE_CHOICES)
    price=models.IntegerField(default=0)
    loc=models.IntegerField(choices=LOCATION_CHOICES,default=1)
    caraddress=models.URLField(max_length=200,default='')
    RC=models.CharField(max_length=20,default='')  
    is_active=models.BooleanField(default=True, verbose_name="Is_Availabel")  
    cimage=models.ImageField(upload_to='images')
    cimage2=models.ImageField(upload_to='images')
    cimage3=models.ImageField(upload_to='images')
    cimage4=models.ImageField(upload_to='images')



def __str__(self):
        return self.carname

class Contact(models.Model):
      name=models.CharField(max_length=30)
      email=models.CharField(max_length=254)
      pnumber=models.CharField(max_length=12)
      message=models.TextField(max_length=500)

def __str__(self) :
        return self.name
 


class Booking(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE,db_column='user')
    car_id = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    hours = models.PositiveIntegerField()
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_rent = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"Booking for car {self.car_id} by {self.user.username}"

class CustomerReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
#     revid=models.ForeignKey('auth_user',on_delete=models.CASCADE,db_column='revid')
    name = models.CharField(max_length=100)
    cimage=models.ImageField(upload_to='images',default='')
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self) :
        return self.name
      
