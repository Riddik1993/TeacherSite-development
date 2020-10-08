from django import forms
from django.forms import ModelForm
from .models import Lesson,ArticleComment,VPR,Category,Direction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha . fields import CaptchaField

class LessonForm(ModelForm):
    captcha=CaptchaField(label='Текст с картинки',error_messages={'invalid': 'Неверный текст с картинки!'})
    class Meta:
        model=Lesson
        fields=('Person_name','lesson_category','Person_phone','Person_email','lesson_date','comments')
        widgets = {
            'lesson_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})}

class ArticleCommentForm(ModelForm):
    captcha=CaptchaField(label='Текст с картинки',error_messages={'invalid': 'Неверный текст с картинки!'})

    class Meta:
        model=ArticleComment
        fields=('Person_name','Person_email','comments','Article')
        exclude=('publish','Article')

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
  username=forms.CharField(max_length=50,label='Логин')
  captcha=CaptchaField(label='Текст с картинки',error_messages={'invalid': 'Неверный текст с картинки!'})
  #last_name=forms.CharField('Фамилия', max_length=150)

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2','first_name','last_name' )

#form for VPR-filter
class VPRchoiceform(ModelForm):
    direct=forms.ModelChoiceField(queryset=Direction.objects.exclude(direction_name='ОГЭ').
                                    exclude(direction_name='ЕГЭ'))

    class Meta:
        model=VPR
        exclude=('name','descr','file','pub_date')
