from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage


# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        email=data['email']

        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Sorry Email in use, choose another one'}, status=409)
        
        
        return JsonResponse({'email_valid': True})
    
    
class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'Username should only contain alphanueric characters'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry Username in use, choose another one'}, status=409)
        
        
        return JsonResponse({'username_valid': True})
    

class RegistrationView(View):
    def get(self, request):
        return render (request,'authentication/register.html')
    
    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        context = {
            'fieldValues' : request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if password1 != password2 or len(password1) < 6 or len(password2) < 6 :
                    messages.error(request,'Passwords not the same or too short')
                    return render (request,'authentication/register.html', context)
                
                user = User.objects.create_user(
                    username=username,
                    email=email,
                )
                user.set_password(password1)
                user.set_active = False
                user.save()

                #send email
                email_subject = 'Activate your account'
                email_body = 'Test Body'

                email = EmailMessage(
                    email_subject,
                    email_body,
                    "goda61@gmail.com",
                    [email],
                    fail_silently=False,
                )
                email.send()

                messages.success(request,'Account Created successfully ...')
                return render (request,'authentication/register.html')
            
        return render (request,'authentication/register.html')