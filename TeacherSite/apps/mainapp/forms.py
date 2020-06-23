
from django.forms import ModelForm
from .models import FeedBack
from captcha . fields import CaptchaField

class GuestFeedBackForm(ModelForm):
    captcha=CaptchaField(label='Текст с картинки',error_messages={'invalid': 'Неправильный текст!'})


    class Meta:
        model=FeedBack
        exclude=('pub_date','publish')
