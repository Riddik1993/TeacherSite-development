
from .models import MemSocial_Article,Memhis_Article,SelfInfo,MainInfo,Category,Shema,Lesson,ArticleComment,Event,\
Conspect,LiterSource,CHeckList,Direction_CHL,OnlineTest,Direction,TestQuestion,Answer,Test_result,MP_new,Schema_subcategory, \
Img_reminder
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#генерит контекст для шаблона онлайн-теста на основании номера теста в базе
def generate_context_for_test_by_testid(test_id):
    test=OnlineTest.objects.get(id=test_id)
    question_list=TestQuestion.objects.filter(test=test_id)
    quest_nums2=[0]
    for q in question_list:
        quest_nums2.append(q.id)
        answer_list=Answer.objects.filter(question__in=quest_nums2)
    context={'test':test,'question_list':question_list,'answer_list':answer_list}
    return context

def send_mail_to_teacher(topic,message):
    send_mail(topic,message, settings.EMAIL_HOST_USER, [str(settings.TEACHER_EMAIL),],fail_silently=True)

def paginate(request,obj_list,obj_per_page):
    page_num=request.GET.get('page')
    paginator=Paginator(obj_list,obj_per_page)
    try:
        pag_list=paginator.page(page_num)
    except EmptyPage:
        pag_list=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        pag_list=paginator.page(1)
    return pag_list



 
