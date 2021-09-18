from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout



# Create your views here.

def loginView(request):
    return render(request,"members/login.html")

def signupView(request):
    return render(request,"members/signup.html")

def loginForm(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        
        user = authenticate(username = username , password = password )

        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'DEAR USER, YOU HAVE LOGIN SUCCESFULLY !!')
            return redirect("/")

        else:
            messages.add_message(request, messages.ERROR, 'EMAIL OR PASSWORD IS NOT VALID. PLEASE ENTER VALID EMAIL OR PASSWORD ')
            return redirect("/account/login/")
    else:
        messages.add_message(request, messages.ERROR, 'PLEASE LOGIN..')
        return redirect("/account/login/")
    

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email= request.POST.get("email")
        pass1= request.POST.get("pass1")
        pass2= request.POST.get("pass2")
        f_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")

        # validationssssss
        # if not (User.objects.get(username=username)==None): 
        #     messages.add_message(request, messages.INFO, 'Username already exist.')
        #     return redirect("/account/signup/")           
            

        if(not(len(pass1)>7 and not pass1.isalnum())):
            messages.add_message(request, messages.INFO, 'PASSWORD MUST BELONGER THEN 8 CHARACTERS AND SHOULD CONTAIN A SYMBOL ...')
            return redirect("/account/signup/")
        
        if(not(pass1==pass2)):
            messages.add_message(request, messages.INFO, 'BOTH THE ENTERED PASSWORD MUST BE SOME')
            return redirect("/account/signup/")

        else:
            try:
                newUser = User.objects.create_user(username,email,pass1)
                newUser.first_name = f_name
                newUser.last_name = last_name
                newUser.save()
                messages.add_message(request, messages.SUCCESS, 'DEAR USER, YOUR ACCOUNT HAS BEEN SUCCSESSFULLY CREATED. PLEASE LOGIN TO CONTINUE....')
                return redirect("/account/login/")
            except Exception as e:
                messages.add_message(request, messages.ERROR, e)
                return redirect("/account/signup/")            
    else:
        messages.add_message(request, messages.ERROR, 'PLEASE SIGNIN TO CONTINUE WITH US....')
        return redirect("/account/signup/")

def Logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'LOG-OUT SUCCESSFULLY !!')
    return redirect("/")