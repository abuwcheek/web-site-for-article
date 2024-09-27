from django.urls import path
from .views import all_news, detail, category, category_detail, create_article, update_article, delete_article, delete_ar, my_articles, person_profile



app_name = "home"
urlpatterns = [
     path('', all_news, name='all'),
     path('categories/', category, name='categories'),
     path('category/<str:slug>/', category_detail, name='category'),

     path('news/<str:slug>/', detail, name='detail'),
     path('create-new/', create_article, name='createar'),
     path('update-new/<str:slug>/', update_article, name="updatear"),
     path('delete-new/<str:slug>/', delete_article, name="deletear"),
     path('delete/<str:slug>/', delete_ar, name="delete"),
     path('my-articles/', my_articles, name='myarticles'),
     path('person-profile/<str:username>/', person_profile, name='personprofile'),
]