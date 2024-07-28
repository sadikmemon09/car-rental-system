from django.contrib import admin
from .models import Car,Contact,CustomerReview,Booking

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display=['id','carname','transmission','fuel','seats','price','loc','caraddress','is_active','cimage','cimage2','cimage3','cimage4']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','pnumber']


class review(admin.ModelAdmin):
    list_display=['id','name','cimage','email','rating','comment','created_at']

class BookingAdmin(admin.ModelAdmin):
    list_display=['id','user','car_id','datetime','hours','car_price','total_rent','payment_id','payment_status']

admin.site.register(Car,CarAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Booking,BookingAdmin)

admin.site.register(CustomerReview,review)

