from cProfile import label
from dataclasses import fields
from email.policy import default
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from .models import signin


class signup(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    password1 = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1', 'first_name', 'last_name']
 
 
class signin(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
                    
# #SIGNUP FORM
# class SignUpForm(forms.ModelForm):
#     class Meta:
#       model = signup
#       fields = ['username', 'email', 'password', 'confirmpassword']
      
#     def validateuser(signup):
        
          


#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         user_count = User.objects.filter(email = email).count()

#         if user_count > 0:
#             raise forms.ValidationError('Email already exists.')
#         return email

                                    
#     def save(self, commit = True):
#         user = super(SignUpForm, self).save(commit = False)
#         user.set_password(self.cleaned_data['password1'])
#         user.email = self.cleaned_data['email']
#         user.username = self.cleaned_data['username']

#         return user

# '''ModelForm allows users to update their info to the database'''
# #Update email and username
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']