from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from PIL import Image
from .models import User

class CastumAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))


class UserRegisterForm(forms.ModelForm):
     username=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'username'}))
     first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Abdullo'}))
     last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Istamov'}))
     email=forms.EmailField(widget=EmailInput(attrs={'class':'validate', 'placeholder':'user123@gmail.com'}))
     phone=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'+998937151034'}))
     image_user=forms.ImageField()



     password = forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'password'}))
     confirm_password = forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'confirm password'}))


     class Meta:
          model = User
          fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'image_user')     


     def clean_username(self):
          username = self.cleaned_data.get('username')
          if User.objects.filter(username=username).exists():
               raise forms.ValidationError("Bu username oldin ro'yxatdan o'tgan")
          return username


     def clean_email(self):
          email = self.cleaned_data.get('email')
          if User.objects.filter(email=email).exists():
               raise forms.ValidationError("Bu email oldin ro'yxatdan o'tgan")
          return email


     def clean_confirm_password(self):
          password = self.cleaned_data.get('password')
          confirm_password = self.cleaned_data.get('confirm_password')
          if password != confirm_password:
               raise forms.ValidationError("Parollar bir-biriga mos emas")
          return confirm_password

     
     def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['confirm_password'])
        user.save()

          # image resize

        img = Image.open(user.image_user.path)
        if img.height>300 or img.width>300:
             new_img = (300, 300)
             img.thumbnail(new_img)
             img.save(user.image_user.path)

        return user



class UserUpdateForm(forms.ModelForm):
     first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Abdullo'}))
     last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Istamov'}))
     phone=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'+998937151034'}))
     image_user=forms.ImageField()


     class Meta:
          model = User
          fields = ('first_name', 'last_name', 'phone', 'image_user')     



     def save(self, commit=True):
          user=super().save(commit)

     #    save funksiyani return dan oldin yozsayam bo'ladi hozir yozsayama bo'ladi
          user.save()
          # image resize

          img = Image.open(user.image_user.path)
          if img.height>500 or img.width>500:
               new_img = (500, 500)
               img.thumbnail(new_img)
               img.save(user.image_user.path)

          return user



# def validate_password_length(form):
#      if len(form) < 8:
#           raise ValidationError("Password 8ta belgidan kam bo'lmasligi lozim")


class ChangePasswordForm(forms.ModelForm):
     password=forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'password'}))
     confirm_password=forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'confirm password'}))

     class Meta:
          model = User
          fields = ('password', 'confirm_password')

     def clean_confirm_password(self):
          password = self.cleaned_data.get('password')
          confirm_password = self.cleaned_data.get('confirm_password')
          if password != confirm_password:
               raise forms.ValidationError("Parollar bir-biriga mos emas")
          elif len(confirm_password) < 8:
               raise forms.ValidationError("Password 8ta belgidan kam bo'lmasligi lozim")
          return confirm_password

     def save(self, commit=True):
          confirm_password = self.cleaned_data.get('confirm_password')
          self.instance.set_password(confirm_password)
          self.instance.save()
          return self.instance