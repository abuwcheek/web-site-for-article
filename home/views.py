from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Article, Category
from account.models import User
from .form import ArticleForm


def before_index(request):
     return render(request, 'before_index.html')



def category(request):
     categories = Category.objects.all()
     context = {
          'categories': categories,
     }
     return render(request, 'category_list.html', context)



def category_detail(request, slug):
     category = get_object_or_404(Category, slug=slug)
     categoryy = category.category_news.all()

     context = {
          'category': category,
          'categoryy': categoryy,
     }
     return render(request, 'category_detail.html', context)



def all_news(request):
     news = Article.objects.all().order_by('-created_at')
     

     context = {
          'news': news,
     }
     return render(request, 'all_news.html', context)



def detail(request, slug):
     detailnews = get_object_or_404(Article, slug=slug)
     detailnews.views += 1
     detailnews.save()

     other_news = Article.objects.all().exclude(slug=slug).order_by('-views')[:3]

     context = {
          'detailnews': detailnews,
          'other_news': other_news,
     }
     return render(request, 'detail.html', context)



def create_article(request):
     if request.method == 'GET':
          form = ArticleForm()

          context = {
               'form': form,
          }
          return render(request, 'create_article.html', context)

     elif request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
          messages.success(request, 'Article yaratildi')
          return redirect('home:all')
     


def update_article(request, slug):
     if request.method == 'GET':
          update_ar = get_object_or_404(Article, slug=slug)
          form = ArticleForm(instance=update_ar)

          context = {
               'slug': update_ar.slug,
               'form': form,
          }
          return render(request, 'update.html', context)

     elif request.method == 'POST':
          updated_ar = get_object_or_404(Article, slug=slug)
          form = ArticleForm(request.POST, request.FILES, instance=updated_ar)

          if form.is_valid():
               form.save()
               messages.success(request, 'Article yangilandi')
               return redirect('home:all')
          else:
               context = {
                    'slug': updated_ar.slug,
                    'form': form
               }
               messages.danger(request, f'Xatolik yuz berdi\n {form.errors}')
               return render(request, 'update.html', context)



def delete_article(request, slug):
     delete_ar = get_object_or_404(Article, slug=slug)
      
     context = {
          'delete_ar': delete_ar,
     }
     return render(request, 'delete.html', context)



def delete_ar(request, slug):
     delete_article = get_object_or_404(Article, slug=slug)
     delete_article.delete()
     messages.warning(request, "Article o'chirildi")
     context = {
          'delete_article': delete_article,
     }
     return redirect('home:all')



def my_articles(request):
     user = request.user
     article_mine = user.user_news.all()

     context = {
          'article_mine': article_mine,
     }
     return render(request, 'my_articles.html', context)



def person_profile(request, username):
     profile = User.objects.get(username=username)
     articlel = profile.user_news.all()

     if request.user == profile:
          context = {
               'article_mine': articlel
          }
          return render(request, 'account/myprofile.html', context)

     context = {
          'profile': profile,
          'articlel': articlel
     }          
     return render(request, 'person_profile.html', context)