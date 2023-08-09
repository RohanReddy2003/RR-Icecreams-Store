from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from app1.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.
def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("login")
    
    return render(request, 'app1/home.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username =username, password= password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request,'app1/login.html')

    return render(request, 'app1/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect(request, 'app1/login.html') 

def home(request):
    return render(request,'app1/home.html')
    # return HttpResponse("This is home page")
def about(request):
    return render(request,'app1/about.html')
    #return HttpResponse("This is about page")
def services(request):
    return render(request,'app1/services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        # print(name,email,desc)
        contact = Contact.objects.create(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your query has been sent!")
    return render(request,'app1/contact.html')
