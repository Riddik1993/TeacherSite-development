from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from articles.models import Category,Direction
from mainapp.models import ExamInfo,LiteratureList,Task,FeedBack
from django.shortcuts import redirect
from .forms import GuestFeedBackForm
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail
from django.conf import settings
from django_q.tasks import AsyncTask,async_task, result
from articles.services import send_mail_to_teacher



def index(request):
    return render(request,'mainapp/index.html')

def ExamInform(request,direction_id,category_id):
    category_list=Category.objects.all()
    try:
        lit_src=LiteratureList.objects.get(lit_direct=direction_id,lit_category=category_id)
    except:
        lit_src=None

    try:
        exam_info=ExamInfo.objects.get(exam_direct=direction_id,exam_category=category_id)
    except:
        exam_info=None

    try:
        task_list=Task.objects.all().filter(task_direct=direction_id,task_category=category_id)
    except:
        task_list=None
    return render(request,'mainapp/exam_info.html',{'category_list':category_list,'exam_info':exam_info,'task_list':task_list,'lit_src':lit_src})

def TaskListing(request,direction_id=3):
    category_list=Category.objects.all()
    exclude_items=('ОГЭ','ЕГЭ')
    try:
        direction_list=Direction.objects.all().exclude(direction_name__in=exclude_items)
    except:
      direction_list=None

    category_task_list=[0]
    for category in category_list:
        task_list=Task.objects.all().filter(task_direct=direction_id,task_category=category.id)
        category_task_list.append(task_list)
    return render(request,'mainapp/tasks.html',{'category_list':category_list,'category_task_list':category_task_list,'direction_list':direction_list})

#добавление отзыва
def FeedBackListing(request):
    feedback_form=GuestFeedBackForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        feedback_form=GuestFeedBackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
                        #отправляем уведомление на почту
            text=request.POST.__getitem__('comments')
            person=request.POST.__getitem__('Person_name')
            message_template='Оставлен новый отзыв о сайте! \n\n  Посетитель: {pers} \
            \n Отзыв:\n\t {com} \n Зайдите в админ-панель и определите, публиковать отзыв или нет'
            message=message_template.format(pers=person,com=text)
            topic='Оставлен новый отзыв о сайте'
            async_task('articles.services.send_mail_to_teacher',topic, message)
            return redirect('success_feedback')

    feedback_list=FeedBack.objects.filter(publish='Y').order_by('pub_date')


    return render(request,"mainapp/feedback.html",{'feedback_list':feedback_list,'feedback_form':feedback_form})









#
