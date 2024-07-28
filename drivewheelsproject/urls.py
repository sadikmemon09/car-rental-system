"""
URL configuration for drivewheelsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drivewheelsapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home/',views.index,name='home'),
    path('register/',views.register),
    path('signin/',views.signin),
    path('signout/',views.signout),
    path('cars/',views.cars),
    path('aboutus/',views.aboutus),
    path('contact/',views.contact),
    path('booking/<cid>/',views.booking,name='booking'),
    path('filterbyfuel/<fid>/',views.filterbyfuel),
    path('filterbytrans/<tid>/',views.filterbytrans),
    path('filterbyseats/<sid>/',views.filterbyseats),
    path('filterbylocation/<lid>/',views.filterbylocation),
    path('sortbyprice/<sp>/',views.sortbyprice),
    path('review/',views.review),
    path('reviewcard/',views.reviewcard),
    path('carbooking/',views.carbooking),
    path('make_payment/', views.make_payment),
    path('paymenthandler', views.paymenthandler,name='paymenthandler'),
    path('mybookings/',views.mybookings),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)