from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Car,Contact,CustomerReview,Booking
from django.db.models import Q
from urllib.parse import urlencode
from django.utils.dateparse import parse_datetime
from django.conf import settings



# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        n=request.POST['name']
        un=request.POST['username']
        num=request.POST['number']
        e=request.POST['email']
        p1=request.POST['password']
        p2=request.POST['password2']

        if n=='' or un=='' or num=='' or e=='' or p1=='' or p2=='':
            messages.error(request,"fields can't be empty" ) 
            return render(request,'register.html')
        elif User.objects.filter(username=un).first():
            messages.error(request,'username already taken')
            return redirect('/register')
        elif User.objects.filter(email=e).first():
            messages.error(request,'email already taken')
            return redirect('/register')
        elif p1 != p2:
            messages.error(request,'password do not match')
            return redirect('/register')
        else:
            u=User.objects.create(username=un,email=e)
            u.set_password(p1)
            u.save()
            messages.success(request,"Your account has been successfully created!")
            return redirect('/signin')
    else:
        return render(request,'register.html') 

def signin(request):
    if request.method=='POST':
        signinusername=request.POST['susername']
        signinpassword=request.POST['spassword']

        if signinusername=='' or signinpassword=='':
            messages.error(request,"field can't be Empty")
            return render(request,'signin.html')
        else:
            user=authenticate(username=signinusername,password=signinpassword)
            if user is not None:
                login(request,user)
                messages.success(request,'congratulations...logged in successfully')
                return redirect('/home')
            else:
                messages.error(request,'invalid credential')
                return redirect('/signin')
    
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('/home')

def cars(request):
    vehicle=Car.objects.all()
    context={}
    context['cars']=vehicle
    return render(request,'cars.html',context)

def filterbyfuel(request,fid):
    q1=Q(is_active=True)
    q2=Q(fuel=fid) 
    # q3=Q(loc=lid)
    context={}
    vehicle=Car.objects.filter(q1 & q2)
    context['cars']=vehicle
    return render(request,'cars.html',context)

def filterbytrans(request,tid):
    q1=Q(is_active=True)
    q2=Q(transmission=tid)
    context={}
    vehicle=Car.objects.filter(q1 & q2)
    context['cars']=vehicle
    return render(request,'cars.html',context)

def filterbyseats(request,sid):
    q1=Q(is_active=True)
    q2=Q(seats=sid)
    context={}
    vehicle=Car.objects.filter(q1 & q2)
    context['cars']=vehicle
    return render(request,'cars.html',context)

def filterbylocation(request,lid):
    q1=Q(is_active=True)
    q2=Q(loc=lid)
    context={}
    vehicle=Car.objects.filter(q1 & q2)
    context['cars']=vehicle
    return render(request,'cars.html',context)

def sortbyprice(request,sp):
    if sp=='0':
        col='price'
    else:
        col='-price'
    vehicle=Car.objects.filter(is_active=True).order_by(col)
    context={}
    context['cars']=vehicle
    return render(request,'cars.html',context)




def aboutus(request):
    return render(request,'aboutus.html')

def booking(request,cid):
    context={}
    if request.user.is_authenticated:
        vehicle=Car.objects.filter(id=cid)
        context['cars']=vehicle
        return render(request,'booking.html',context)
    else:
        return redirect('/signin')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        pnumber=request.POST['phone']
        message=request.POST['message']

        if name=='' or email=='' or pnumber=='' or message=='':
            messages.error(request,"fields can't be empty" ) 
            return render(request,'contact.html')
        else:
            u=Contact.objects.create(name=name,email=email,pnumber=pnumber,message=message)
            u.save()
            messages.success(request,"Your message has been successfully sent! we will try to reach you soon")
            return redirect('/contact')
    else:
        return render(request,'contact.html')
    
# def totalrent(request):
#     if request.method=="POST":
#         pickup=request.POST['pickupdt']
#         dropoff=request.POST['dropoffdt']

#         if pickup=='' or dropoff=='':
#             messages.error(request,"fields can't be empty" ) 
#             return render(request,'booking.html')
#         else:
#             total=totalrent.objects.create(pickupDT=pickup,dropoffDT=dropoff)
#             total.save()
#             messages.success(request,"Your message has been successfully sent! we will try to reach you soon")
#             return redirect('/booking')
#     else:
#         return render(request,'booking.html')


    

def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        image=request.POST['image']
        email = request.POST['email']
        rating = request.POST['rating']
        comment = request.POST['comment']

        if name=='' or email=='' or rating=='':
            messages.error(request,"fields can't be empty" ) 
            return render(request,'reviews.html')
        else:
            r=CustomerReview.objects.create(name=name,cimage=image,email=email,rating=rating,comment=comment)
            r.save()
            messages.success(request,"Your Review has been successfully sent! Thank u for rating Drive Wheels..to see your review go to about us page")
            return redirect('/index')
    else:
        return render(request,'reviews.html')

def reviewcard(request):
    context={}
    rev=CustomerReview.objects.all()
    context['reviews']=rev
    print(rev)
    return render(request,'aboutus.html',context)

def carbooking(request):
    context={}
    if request.method == 'POST':
        dt = request.POST['datetime']
        hr=request.POST['hours']
        car_id=request.POST['car_id']
        car_price=request.POST['car_price']

        print(dt,hr, car_id)

        #print(response.cookies['date'])
        #print(response.cookies['hours'])

        totalRent = int(car_price) * int(hr)
        print(totalRent)

        # response = HttpResponse("Cookie Set")
        # request.COOKIES['rentValue'] = totalRent
        # response.set_cookie('rentValue', totalRent)
        # #print(response.get_cookie('rentValue'))
        # response.set_cookie("rentValue", totalRent, samesite='Lax')
        # tutorial = request.COOKIES.get('rentValue')
        # print(tutorial)
        booking = Booking(
            user=request.user,
            car_id=car_id,
            datetime=parse_datetime(dt),
            hours=int(hr),
            car_price=float(car_price),
            total_rent=totalRent
        )
        booking.save()
        
        query_params = urlencode({'total': totalRent,'booking_id': booking.id})
        #return redirect('/booking/' + car_id + '?rentValue=' + totalRent)
        return redirect(f'/booking/{car_id}?{query_params}')
    else:
        return render(request,'index.html')
    


import razorpay
razorpay_client = razorpay.Client(auth=('rzp_test_r4DR8M94HImm5D','T4gHh7IrrXrEsPqGNT9Vc0Dm'))
def make_payment(request):
    booking_id = request.GET.get('booking_id')
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        amount = int(booking.total_rent * 100)  # Convert to paise

        # Create Razorpay order
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency='INR', payment_capture='1'))
        booking.payment_id = razorpay_order['id']
        booking.save()

        context = {
            'booking': booking,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_merchant_key':'rzp_test_r4DR8M94HImm5D',
            'amount': amount,
            'currency': 'INR',
            'callback_url': 'paymenthandler/',
        }

        return render(request, 'make_payment.html', context)
    else:
        return render(request, 'make_payment.html', {'booking': booking})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
            }

            # Verify the payment signature
            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result is None:
                try:
                    booking = Booking.objects.get(payment_id=order_id)
                    booking.payment_status = 'Paid'
                    booking.save()
                    return render(request, 'payment_success.html', {'booking': booking, 'message': 'Payment was successful!'})
                except Booking.DoesNotExist:
                    print(f"No booking found for payment_id: {order_id}")
                    return render(request, 'payment_fail.html', {'message': 'No booking found for this payment ID'})

            else:
                print("Payment signature verification failed")
                return render(request, 'payment_fail.html', {'message': 'Payment signature verification failed'})

        except Exception as e:
            print(f"Exception: {e}")
            return render(request, 'payment_fail.html', {'message': f'Exception: {e}'})
    else:
        return redirect('/index')

def mybookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'MyBookings.html', {'bookings': bookings})

