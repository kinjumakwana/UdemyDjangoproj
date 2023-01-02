from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email",)
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'demo@gmail.com'}))
#     username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'User123'}))
#     password1= forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
#     password2= forms.CharField(label="Conform Password", required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))

#     class Meta:
#         model=User
#         fields=["username","email"]
    
#     def save(self,commit=True):
#         user=super(NewUserForm,self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email Address'}