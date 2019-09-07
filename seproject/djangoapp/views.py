from django.shortcuts import render
from djangoapp.forms import  NewUser
from django.core.mail import send_mail
from django.conf import settings
from djangoapp.models import User
from . import  forms

# Create your views here.

def index(request):
    return  render(request , 'djangoapp/index.html')

def response(request):
    return render(request , 'djangoapp/response.html')

i = 0

def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        i =0

        if form.is_valid():
            form.save(commit=True)
            recievers =[]
            sender = []
            send=[]
            for user in User.objects.all():
                recievers.append(user.email)
                sender.append(user.text)
            i = len(recievers)-1
            send = ''.join(sender)

            send_mail(
                'Response from shakthi engineering works',
                'Thank you for contacting shakthi engineering works, it means a world to us',
                'harithasbc7@gmail.com',
                [recievers[i], ],
                fail_silently=False,
            )

            send_mail(
                'Response from shakthi engineering works',
                 send,
                'harithasbc7@gmail.com',
                ['harithas201@gmail.com',],
                fail_silently=False,
            )


            return response(request)
        else:
            print('error filling the form')
    return render(request, 'djangoapp/forms.html' ,{'form' : form})



