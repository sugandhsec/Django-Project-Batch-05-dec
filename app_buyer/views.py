from django.shortcuts import render
from app_buyer.models import *
from app_seller.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,"index.html")

import random
def signup(request):
    global name
    name="hello"
    context={}
    if request.method=="POST":
        try:
            user_exist=User.objects.get(email=request.POST["email"])
            context["msg"]="User Already Exist"
        except:

            if request.POST["password"]==request.POST["cpassword"]:
                global otp

                otp=random.randint(100000,999999)
                subject = 'OTP VERIFICATION PROCESS'
                message = f'Thanks for chosing us , your otp is {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST["email"], ]
                send_mail( subject, message, email_from, recipient_list )
                global User_data
                User_data={
                    "username":request.POST["uname"],
                    "email":request.POST["email"],
                    "password":request.POST["password"],
                }
                return render(request,"otp.html")
            else:
                context["msg"]="Password And confirm password not match"
    return render(request,"signup.html",context)

from django.contrib.auth.hashers import make_password,check_password

def otp(request):
    context={}
    if request.method=="POST":
        if otp==int(request.POST["otp"]):
            User.objects.create(
                username=User_data["username"],
                email=User_data["email"],
                password=make_password(User_data["password"]),
            )
            context["msg"]="Signup Succesfull"
            return render(request,"signup.html",context)
        else:
            context["msg"]="Invalid OTP"
    return render(request,"otp.html",context)


def login(request):
    context={}
    if request.method=="POST":
        try:
            current_user=User.objects.get(email=request.POST["email"])
            print(current_user)
            # if current_user.password==request.POST["password"]:
            # check_password("original_value","hashed_value")
            if check_password(request.POST["password"], current_user.password):
                context["msg"]="LOGIN SUCCESFULL"
                request.session["email"]=request.POST["email"]
                user_data=User.objects.get(email=request.session["email"])
                context["user_data"]=user_data
                return render(request,"product.html",context)
            else:
                context["msg"]="Incorrect password"
        except:
            context["msg"]="Invalid User"
    return render(request,"login.html",context)


def logout(request):
    context={}
    del request.session["email"]
    context["msg"]="LOGOUT successfull"
    return render(request,"login.html",context)

def profile(request):
    context={}
    user_data=User.objects.get(email=request.session["email"])
    context["user_data"]=user_data
    if request.method=="POST":
        user_data.username=request.POST["uname"]
        user_data.email=request.POST["email"]
        # password check
        if check_password(request.POST["opassword"],user_data.password):
            if request.POST["npassword"]==request.POST["cnpassword"]:
                user_data.password=make_password(request.POST["npassword"])
            else:
                context["user_data"]="New Password nad confirm New password Not match"
        else:
            context["user_data"]="Old Password Not match"
        # images check
        # try:
        request.FILES["propic"]
        user_data.profile_pic= request.FILES["propic"]
        # except:
        #     pass
        user_data.save()
        context["msg"]="Profile Updated Successfully"
        context["user_data"]=user_data
    return render(request,"profile.html",context)


def product(request):
    context={}
    user_data=User.objects.get(email=request.session["email"])
    context["user_data"]=user_data
    all_product=Product.objects.all()
    context["all_product"]=all_product
    return render(request,"product.html",context)