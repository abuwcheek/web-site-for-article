from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from .forms import CastumAuthForm, UserRegisterForm, UserUpdateForm, ChangePasswordForm
from django.contrib import messages
from PIL import Image
from django.db.models import Q
from .models import User, Contact, About
from home.models import Article



class UserRegisterView(View):
     form = UserRegisterForm

     def get(self,  request):
          if not request.user.is_authenticated:
               context = {
                    'form': self.form
               }
               return render(request, 'account/register.html', context)
          messages.warning(request, 'Siz avval tizimdan chiqishingiz kerak')
          return redirect('home:all')


     def post(self, request):
          user_form = self.form(data=request.POST, files=request.FILES)
          if user_form.is_valid():
               user_form.save()
               messages.success(request, 'Accaunt muvaffaqqiyatli yaratildi')
               return redirect('home:all')

          messages.warning(request, 'Accaunt yaratilmadi')
          context={
               'form':user_form,
               }
          return render(request, 'account/register.html', context)


def register(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, f"Account {username} uchun yaratildi")
               return redirect('home:all')
          else:
               messages.warning(request, f"Xatolik yuz berdi:\n {form.errors}")
               return render(request, 'account/register.html', {'form': form})
     else:
          form = UserCreationForm(request.POST)
          
     return render(request, 'account/register.html', {'form': form})



class MyProfileView(View):
     def get(self, request):
          if request.user.is_authenticated:
               user = User.objects.get(id=request.user.id)
               contex = {
                    'user': user
               }
               return render(request, 'account/myprofile.html', contex)
          messages.warning(request, 'Siz oldin tizimga kirishingiz kerak')
          return redirect('account:signin')



class UpdateUserView(View):
     form = UserUpdateForm
     def get(self, request):
          if request.user.is_authenticated:
               user = User.objects.get(id=request.user.id)
               context = {
                    'form': self.form(instance=user)
               }
               return render(request, 'account/update-profile.html', context)
          messages.warning(request, 'Siz avval tizimga kirishingiz kerak')
          return redirect('account:signup')


     def post(self, request):
          user_form = self.form(data=request.POST, files=request.FILES, instance=request.user)
          if user_form.is_valid():
               user_form.save()
               messages.success(request, 'Accaunt muvaffaqqiyatli yangilandi')
               return redirect('account:myprofile')

          messages.warning(request, 'Accaunt yangilanmadi')
          context={
               'form':user_form,
               }
          return render(request, 'account/update-profile.html', context)



class ChangePasswordView(View):
     form = ChangePasswordForm
     def get(self, request):
          if request.user.is_authenticated:
               user = User.objects.get(id=request.user.id)
               context = {
                    'form': self.form,
               }
               return render(request, 'account/change_password.html', context)
          else:
               messages.warning(request, 'Siz oldin login qilishingiz kerak')
               return redirect('account:signin')

     def post(self, request):
          password_form = self.form(data=request.POST, instance=request.user)
          if password_form.is_valid():
               password_form.save()
               login(request, request.user)
               messages.success(request, 'Password muvaffaqqiyatli yangilandi')
               return redirect('account:myprofile')

          messages.warning(request, 'Password yangilanmadi')
          context={
               'password_form':form,
               }
          return render(request, 'account/change_password.html', context)


class LoginView(View):
     def get(self, request):
          if request.user.is_authenticated:
               return redirect('home:all')

          form = CastumAuthForm
          context = {
               'form': form,
          }
          return render(request, 'account/login.html', context)


     def post(self, request):
          data = request.POST
          form = CastumAuthForm(data=data)
          if form.is_valid():
               user = form.get_user()
               login(request, user)
               messages.success(request, 'Tizimga muvaffaqqiyatli kirdingiz')
               return redirect('home:all')
          else:
               messages.warning(request, 'Parol yoki login xato')
               return render(request, 'account/login.html', {'form':form})


class LogoutView(View):
     def get(self, request):
          logout(request)
          messages.warning(request, 'Tizimdan muvaffaqqiyatli chiqtingiz')
          return redirect('home:all')





class ContactView(View):
     def get(self, request):
          return render(request, 'contact.html')

     def post(self, request):
          data = request.POST
          contact = Contact()
     
          contact.name = data.get('name')
          if not contact.name:
               messages.warning(request, "Maydonlar bo'sh bo'lmasligi lozim")
               return render(request, 'contact.html')

          contact.email = data.get('email')
          if not contact.email:
               messages.warning(request, "Maydonlar bo'sh bo'lmasligi lozim")
               return render(request, 'contact.html')

          contact.phone = data.get('phone')
          if not contact.phone:
               messages.warning(request, "Maydonlar bo'sh bo'lmasligi lozim")
               return render(request, 'contact.html')

          contact.subject = data.get('subject')
          if not contact.subject:
               messages.warning(request, "Maydonlar bo'sh bo'lmasligi lozim")
               return render(request, 'contact.html')

          contact.message = data.get('message')
          if not contact.message:
               messages.warning(request, "Maydonlar bo'sh bo'lmasligi lozim")
               return render(request, 'contact.html')

          contact.save()

          messages.success(request, 'Sizning malumotlaringiz yuborildi')
          return render(request, 'contact.html')




class AboutView(View):
     def get(self, request):
          about = About.objects.all()
          context = {
               'about': about,
          }

          return render(request, 'contact.html', context)
     



class SearchView(View):
    def get(self, request):
          query = request.GET.get('search')
          print(query)
          if not query:
               return redirect('home:all')

          news = Article.objects.all().filter(Q(title__icontains = query) | Q(subtitle__icontains = query) | Q(body__icontains = query))
          if not news:
               messages.warning(request, "So'rov bo'yicha ma'lumot topilmadi")
               return redirect('home:all')

          context = {
               'searchnews': news 
          }
          messages.info(request, 'Siz izlagan xabarlar')
          return render(request, 'search_news.html', context)

