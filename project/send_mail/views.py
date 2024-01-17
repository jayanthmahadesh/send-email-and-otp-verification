from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail('Hello from jayanth',
    'hello there , this is automated message.',
    'computeruse777@gmail.com',
    ['loyopiv424@wentcity.com'],
    fail_silently=False)
    return render(request,'index.html')