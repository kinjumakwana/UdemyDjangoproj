from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
# def register(request):  
#     if request.method=='POST':
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print('Account created')
#             return redirect('myapp/Products')
#     else:
#         form = RegisterForm()
#     context={
#         'form':form,
#     }
#     return render(request, "users/register.html", context)



# def register1(request):  
#     if request.POST == 'POST':  
#         form = UserCreationForm()  
#         if form.is_valid():  
#             form.save()  
#         messages.success(request, 'Account created successfully')  
  
#     else:  
#         form = UserCreationForm()  
#     context = {  
#         'form':form  
#     }  
#     return render(request, 'register.html', context)  

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'You have successfully created account!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'users/sign_up.html', {'form': fm})  

# @login_required(login_url='user:login')
# @login_required(login_url='/users/login')
@login_required
def profile(request):
    return render(request, "users/profile.html")

def createprofile(request):
    if request.method=='POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user=request.user
        profile = Profile(user=user,contact_number=contact_number, image=image)
        profile.save()
    return render(request,"users/createprofile.html")

def seller_profile(request,id):
    seller=User.objects.get(id=id)
    context={ 
        'seller':seller,
    }
    return render(request, "users/seller_profile.html",context)