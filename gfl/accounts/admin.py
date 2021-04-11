from django.contrib import admin
from .models import CustomUser
from .models import OTPVerifiaction
from django.contrib.auth.admin import UserAdmin


class CustomUserConfig(UserAdmin):
    model = CustomUser
    list_display = ('email','user_name','contact_number')


class OTPVerifiactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number','otp', 'is_verfied')


admin.site.register(CustomUser)

admin.site.register(OTPVerifiaction,OTPVerifiactionAdmin)
