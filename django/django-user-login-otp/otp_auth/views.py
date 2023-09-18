import pyotp
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .models import OTP

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        
        if user:
            # Generate OTP
            otp_secret = pyotp.random_base32()
            otp = pyotp.TOTP(otp_secret)
            otp_code = otp.now()

            # Save OTP to the database
            otp_obj, created = OTP.objects.get_or_create(user=user, email=email)
            otp_obj.otp_secret = otp_secret
            otp_obj.save()

            # Send OTP via email
            subject = 'Your OTP for Login'
            message = f'Your OTP for login is: {otp_code}'
            from_email = 'your@email.com'  # Update with your email
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('verify_otp')
        else:
            return render(request, 'send_otp.html', {'message': 'Email not found'})
    else:
        return render(request, 'send_otp.html')

import pyotp
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import OTP

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp_code = request.POST.get('otp')
        
        otp_obj = OTP.objects.filter(email=email).first()
        
        if otp_obj:
            otp = pyotp.TOTP(otp_obj.otp_secret)
            print(otp_obj.otp_secret)
            print(otp_code)
            print(otp.verify(otp_code))
            if otp.verify(otp_code):
                otp_obj.is_verified = True
                otp_obj.save()
                user = authenticate(request, username=otp_obj.user.username, password='')
                if user:
                    login(request, user)
                    return redirect('home')  # Replace 'home' with the URL name of your home page
                else:
                    return redirect('login')  # Replace 'login' with the URL name of your home page
            else:
                return render(request, 'verify_otp.html', {'message': 'Invalid OTP'})
        else:
            return render(request, 'verify_otp.html', {'message': 'OTP not found'})
    else:
        return render(request, 'verify_otp.html')
