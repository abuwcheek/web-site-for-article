from django import forms
from .models import Article 



class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title', 'required':True}))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={'class':'from-control', 'placeholder':'Subtitle', 'required':True}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body', 'required':True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'required':False, 'accept':'image/*'}))

    
    class Meta:
          model=Article
          fields=('author', 'category', 'title', 'subtitle', 'body', 'image')


          def clean_title(self):
               title = self.cleaned_data.get('title')
               if len(title) >= 10:
                    raise('Title is short')
               return title

          def save(self, commit=True):
               instance=super(NewsForm, self).save(commit=False)
               if commit:
                    instance.save()
               return instance  
