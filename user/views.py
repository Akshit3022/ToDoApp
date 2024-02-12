from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from . models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    user_email = request.session.get('email')
    if user_email:
        user_instance = get_object_or_404(CustomUser, email=user_email)
        addTask = Task.objects.filter(user_id=user_instance) 
        return render(request, 'home.html', {'addTask': addTask})
    else:
        return redirect('login')
    

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 

        user = request.user

        if CustomUser.objects.filter(email=email, password=password).exists():  
            request.session['email'] = email
            return redirect('home')
        elif User.objects.filter(email=user.email).exists() and check_password(password, request.user.password):
            request.session['email'] = email
            return redirect('adminDash')
        else:
            return HttpResponse("Either email or password is incorrect.")
              
    return render(request, 'login.html')
    

def register(request):
    if request.method == 'POST':

        email = request.POST.get('email')

        if CustomUser.objects.filter(email=email).exists():
            return HttpResponse("User Already Exists")

        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser(name=name, email=email, password=password)
        user.save()
        request.session['email'] = email
        return redirect('login')
    
    return render(request,'register.html')


@login_required
def add(request):
    if request.method == 'POST':
        date = datetime.date.today()
        task = request.POST.get('task')
        description = request.POST.get('description')

        obj = CustomUser.objects.get(email=request.session['email'])
        user_instance = get_object_or_404(CustomUser, id=obj.id)

        obj = Task.objects.create(user_id=user_instance, date=date, task=task, description=description)
        obj.save()
        
        return redirect('home')

    return render(request, 'home.html')


def completeTask(request, id):
    task = Task.objects.get(id=id)
    task.completed = True

    if task.completed == True:
        task.status = "Completed"

    Task.objects.filter(status=task.status) 
    task.save()

    return redirect('home')


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')    


def logout(request):
    del request.session['email']
    return render(request, 'login.html')


def adminDash(request):

    users = CustomUser.objects.all()
    return render(request, 'adminDash.html', {'users': users})


def displayTask(request, id):
    tasks = Task.objects.filter(user_id=id)
    # tasks.save()
    return render(request, 'displayTask.html' ,{'tasks':tasks})