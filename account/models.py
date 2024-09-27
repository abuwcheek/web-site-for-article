from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator




class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateField(auto_now=True)
     is_active = models.BooleanField(default=True)

     class Meta:
          abstract = True



class User(AbstractUser):
     phone = models.CharField(max_length=15, null=True, blank=True)
     image_user = models.ImageField(upload_to='user_avatar/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'heic'))])
     

     @property
     def full_name(self):
          return f'{self.first_name} {self.last_name}'

     def hashin_password(self):
          if not self.password.startswith('pbkdf2_sha256'):
               self.set_password(self.password)


     def save(self, *args, **kwargs):
          self.hashin_password()
          return super().save(*args, **kwargs)
          


class About(BaseModel):
     my_about = models.CharField(max_length=50)
     my_location = models.CharField(max_length=500)
     my_email = models.EmailField()
     my_phone = models.CharField(max_length=15)
     
     linkedin=models.CharField(max_length=100)
     facebook=models.CharField(max_length=100)
     youtube=models.CharField(max_length=100)
     instagram=models.CharField(max_length=100)

     def __str__(self):
          return self.my_about

     class Meta:
          verbose_name = "About"



class Contact(BaseModel):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     phone =  models.CharField(max_length=15)
     subject = models.CharField(max_length=200)
     message = models.TextField()



     def __str__(self):
          return str(self.name)