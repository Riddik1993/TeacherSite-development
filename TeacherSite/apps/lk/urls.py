from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.ShowProfile,name='Profile'),
    path('mytests/',views.Show_LK_Tests,name='LK_Tests'),
    path('favor/',views.Show_LK_Favor,name='LK_favor')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
