from django.shortcuts import render, HttpResponse
from test1.forms import File_Upload_Form
from registration.forms import User_Profile_Form,User_Profile_Login_Form

# Create your views here.
def user_document(request):
    user=File_Upload_Form()
    if request.method=='POST':
        user=File_Upload_Form(request.POST,request.FILES)
        if user.is_valid():
            user.save()
            return HttpResponse('<h1> file is uploaded</h1>')
    else:
        user=File_Upload_Form()
    return render(request,'templates/registration/user_login.html',{'user':user})

def signup(request):
    user=User_Profile_Form()
    if request.method=='POST':
        user=User_Profile_Form(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponse('<h1> singup done</h1>')
    else:
        user=User_Profile_Form()
    return render(request,'templates/registration/user_reg.html',{'user':user})

def userlogin(request):
    user=User_Profile_Login_Form()
    if request.method=='POST':
        user=User_Profile_Login_Form(request.POST)
        if user.is_valid():
            pass
    else:
        user=User_Profile_Login_Form()
    return render(request,'templates/registration/user_log.html',{'user':user})
