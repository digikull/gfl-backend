from django.urls import path,include
from accounts import views


urlpatterns = [
    path('checkotp/<str:otp>', views.checkotp ),
    path('sendotp/<str:number>', views.SendOTP ),


]