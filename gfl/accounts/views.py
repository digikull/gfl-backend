from django.shortcuts import render
import os
import random
import math

# * Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

# * Twilio Imports
from twilio.rest import Client




# * Generating OTP


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP

OTP = generateOTP()


# *Checks OTP with the otp recevied from the GET Request


@api_view(['GET'])
def SendOTP(request, number):
    number_with_code = "+91"+number
    
    account_sid = 'AC6593b5edf2aaa3acfcb8e796bd76fd55'
    auth_token = '5e5ed6796e2a67dff536796048073019'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Thank you for Registering on GFL your OTP is "+OTP,
                        from_='+12082617126',
                        to=number_with_code
                    )

    return Response({"msg": "OTP sent"})


@api_view(['GET'])
def checkotp(request, otp):
    print(OTP)
    if OTP == otp:
        return Response({"status": True})
    else:
        return Response({"status": False})
