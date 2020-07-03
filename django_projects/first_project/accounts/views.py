from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching...')
            return redirect('register')

    else:

        return render(request,'reg.html')