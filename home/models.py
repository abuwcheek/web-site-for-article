from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from account.models import User


class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True


class Category(BaseModel):
     name = models.CharField(max_length=200)
     slug = models.SlugField(blank=True, null=True)


     def __str__(self):
          return self.name


     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.name, allow_unicode=True)
          return super().save(*args, **kwargs)


     def get_category_url(self):
          return reverse('category', args=[str(self.slug)])


class Article(BaseModel):
     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_news')
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_news')
     image = models.ImageField(upload_to='images/')
     title = models.CharField(max_length=200)
     slug = models.SlugField(blank=True)
     subtitle = models.CharField(max_length=400)
     body = models.TextField()
     views = models.IntegerField(default=0)


     class Meta:
          verbose_name = "Article"
          verbose_name_plural = "Articles"

     def __str__(self):
          return f"{self.author} | {self.title}"



     def get_absolyute_url(self):
          return reverse('detail', args=[str(self.slug)])
     


     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title, allow_unicode=True)
          return super().save(*args, **kwargs)
