# *
from . utils.otpUtils import generateOTP, generatingOTP
# * Django imports
from django.db import IntegrityError
from django.shortcuts import render

# * models Import
from .models import OTPVerifiaction
from .models import CustomUser

# * Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# * Twilio Imports
# from twilio.rest import Client
import jwt ,datetime


# # * Generating 4-Digit Random Numbers
# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(4):
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP


# # *Checks OTP with the otp recevied from the GET Request
# def generatingOTP(number):
#     number_with_code = "+91"+number
#     OTP = generateOTP()

#     #! Code for Twilio
#     # account_sid = 'AC6593b5edf2aaa3acfcb8e796bd76fd55'
#     # auth_token = 'eff74dbf93b705721502f7fc4a4dbe3f'
#     # client = Client(account_sid, auth_token)

#     # message = client.messages \
#     #                 .create(
#     #                     body="Thank you for Registering on GFL your OTP is "+OTP,
#     #                     from_='+12082617126',
#     #                     to=number_with_code
#     #                 )

#     return OTP


class LoginApi(APIView):
    def post(self, request):
        print(request.data, 'data')
        phone = request.data.get('phone')
        password = request.data.get('password')

        user = User.objects.filter(phone=phone).first()

        if user is None:
            raise AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        payload = {
            'id' : user.id ,
            'exp' : datetime.datetime.utcnow()+ datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token =jwt.encode(payload, "secret", algorithm="HS256")
        response = Response()

        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
           'jwt' : token 
          
            }
        return response

# * Generating the OTP
@api_view(['GET', 'POST'])
def otpGeneration(request):
    number = request.data['number']
    generatedOTP = generatingOTP(number)
    if generatedOTP:
        data = OTPVerifiaction(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"OTPSent": True})
    else:
        return Response({"OTPSent": False})


# * Comparing the User OTP with the OTP stored in DataBase
@api_view(['PUT'])
def checkOTP(request):
    number = request.data['number']
    otp = request.data['otp']
    generatedOTP = OTPVerifiaction.objects.filter(
        phone_number=number).values_list('otp')
    if generatedOTP[0][0] == otp:       #
        try:
            data = OTPVerifiaction.objects.get(phone_number=number)

        except OTPVerifiaction.DoesNotExist as error:
            return Response({"Error": error})

        data.is_verfied = True
        data.save()
        return Response({"status": True})

    else:
        return Response({"status": False})


# * Registering the user & deleting the verified OTP
@api_view(['POST'])
def registerUser(request):
    if 'username' in request.data:
        user_name = request.data['username']
    else:
        return Response({"Error": "Username Not Provided"})

    if 'email' in request.data:
        email = request.data['email']
    else:
        return Response({"Error": "Email Not Provided"})

    if 'number' in request.data:
        contact_number = request.data['number']
    else:
        return Response({"Error": "Contact Number Not Provided"})

    if 'password' in request.data:
        password = request.data['password']
    else:
        return Response({"Error": "Password Not Provided"})

    user = CustomUser(user_name=user_name)
    user.email = email
    user.contact_number = contact_number
    user.set_password(password)
    try:
        user.save()
        otp_clutter = OTPVerifiaction.objects.get(phone_number=contact_number)
        otp_clutter.delete()
        return Response({"IntegrityError": False})
    except IntegrityError as e:
        return Response({"IntegrityError": True})
