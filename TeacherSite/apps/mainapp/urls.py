from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='articles/')),
    path('feedback/',views.FeedBackListing,name='FeedBackListing'),
    path('articles/',include('articles.urls')),
    path('question/',TemplateView.as_view(template_name="mainapp/question.html"),name='question'),
    path('tasks/<int:direction_id>',views.TaskListing,name='taskinfo'),
    path('tasks/',views.TaskListing,name='taskinfo'),
    path('exams/<int:direction_id>/<int:category_id>',views.ExamInform,name='examinfo'),
    path('successfeed/',TemplateView.as_view(template_name='mainapp/success_feedback.html'),name='success_feedback')
]
