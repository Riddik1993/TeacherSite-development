import datetime
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import MemSocial_Article,Memhis_Article,SelfInfo,MainInfo,Category,Shema,Lesson,ArticleComment,Event,\
Conspect,LiterSource,CHeckList,Direction_CHL,OnlineTest,Direction,TestQuestion,Answer,Test_result,MP_new,Schema_subcategory, \
Img_reminder,AnswerRecieved,VPR
from .services import generate_context_for_test_by_testid
from mainapp.models import Task
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.edit import CreateView
from .forms import LessonForm,ArticleCommentForm,SignUpForm,VPRchoiceform
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from calendar import HTMLCalendar
from .utils import EventCalendar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from itertools import chain
from operator import attrgetter
import os

#памятки по истории и обществознанию
def MemSocialList(request):
    Memsocial_Article_list=MemSocial_Article.objects.order_by('-pub_date')
    paginator=Paginator(Memsocial_Article_list,5)
    num_page=request.GET.get('page')
    image=Img_reminder.objects.get(type='S')
    try:
        image=Img_reminder.objects.get(type='S')
    except:
        image=()
    try:
        articles=paginator.page(num_page)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles=paginator.page(1)

    return render(request,'articles/MemSocial.html',{'articles':articles,'image':image})

def MemSocialDetail(request,article_id):
    a=MemSocial_Article.objects.get(id=article_id)
    return render(request,'articles/MemSocialdetail.html',{'article':a})

def MemHistory(request):
    Memhis_Article_list= Memhis_Article.objects.order_by('-pub_date')
    paginator=Paginator(Memhis_Article_list,5)
    num_page=request.GET.get('page')


    try:
        image=Img_reminder.objects.get(type='H')
    except:
        image=()



    try:
        articles=paginator.page(num_page)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles=paginator.page(1)

    return render(request,'articles/MemHistory.html',{'articles':articles,'image':image})

def MemHistoryDetail(request,article_id):
    comment_form=ArticleCommentForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        comment_form=ArticleCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            art=Memhis_Article.objects.get(id=article_id)
            new_comment.Article= Memhis_Article.objects.get(id=article_id)
            new_comment.save()
            #отправляем уведомление на почту
            text=request.POST.__getitem__('comments')
            person=request.POST.__getitem__('Person_name')
            art_name=art.article_title

            message_template='Оставлен новый комментарий к памятке по истории! \n\n Памятка:{rem} \n Посетитель: {pers} \
            \n Комментарий:\n\t {com} \n Зайдите в админ-панель и определите, публиковать или нет'
            message=message_template.format(rem=art_name,pers=person,com=text)
            send_mail('новый комментарий к памятке по истории', message, settings.EMAIL_HOST_USER, ['Na5tyu5ha@mail.ru'],fail_silently=True)

            return redirect('success_comment')
    try:
        a=Memhis_Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    comments_list=ArticleComment.objects.filter(Article_id=a.id,publish='Y').order_by('-id')[:10]
    return render(request,"articles/MemHistorydetail.html",{'article':a,'comments_list':comments_list,'comment_form':comment_form})
#информация о себе
def About(request):
    try:
        a=SelfInfo.objects.first()
    except:
        raise Http404("Информация о себе пока не добавлена")
    return render(request,"articles/about.html",{'article':a})

#информация на главной странице
def ShowMainInfo(request):
    try:
        a=MainInfo.objects.first()
    except:
        raise Http404("Информация на главную страницу пока не добавлена")

    task_list=Task.objects.all()
    MemHistory_list=Memhis_Article.objects.all()
    MemSocial_list=MemSocial_Article.objects.all()
    Shema_list=Shema.objects.all()
    CheckLists=CHeckList.objects.all()
    OnlineTests=OnlineTest.objects.all()
    Conspects=Conspect.objects.all()
    LiterSources=LiterSource.objects.all()

    publications_list=sorted(chain(MemHistory_list,MemSocial_list,Shema_list,CheckLists,
                             OnlineTests,task_list,Conspects,LiterSources),
                             key=attrgetter('pub_date'),
                             reverse=True)[:5]


    news_list=MP_new.objects.all()

    return render(request,"articles/MainPage.html",{'article':a,'task_list':task_list,
    'publications_list':publications_list,'news_list':news_list})

#Выводит список литературы
def ShowLiteratureList(request):
    Lit_list=RecommendBook.objects.order_by('id')
    return render(request,'articles/literature.html',{'Lit_list':Lit_list})

#подкатегории схем
def   ShowShemasSubcat(request,cat_id):
    category_list=Category.objects.all()
    Subcat_list=Schema_subcategory.objects.filter(category=cat_id)
    paginator=Paginator(Subcat_list,9)
    num_page=request.GET.get('page')
    try:
        subcategories=paginator.page(num_page)
    except EmptyPage:
        subcategories=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        subcategories=paginator.page(1)


    return render(request,'articles/shemas_subcat.html',{'subcategories':subcategories,'category_list':category_list})

#VPR
def   ShowVpr(request):
    if request.method == 'POST':
        form=VPRchoiceform(request.POST)
        subject=request.POST.get('category')
        direction=request.POST.get('direct')
        type=request.POST.get('type')
        VPRs=VPR.objects.filter(category=subject,direct=direction,
                                      type=type)
    else:
        VPRs=VPR.objects.all()
        form=VPRchoiceform()

    paginator=Paginator(VPRs,10)
    num_page=request.GET.get('page')

    try:
        VPR_list=paginator.page(num_page)
    except EmptyPage:
        VPR_list=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        VPR_list=paginator.page(1)


    return render(request,'articles/vpr.html',{'VPR_list':VPR_list,'form':form})


#Пагинатор для схем
def ShowShemas(request,cat_id,subcat_id):
    subcat_obj=Schema_subcategory.objects.get(id=subcat_id)
    subcat_name=subcat_obj.subcategory_name
    cat_obj=Category.objects.get(id=cat_id)
    cat_name=cat_obj.category_name
    shemas_list=Shema.objects.filter(shema_category=cat_id,schema_subcategory=subcat_id)
    category_list=Category.objects.all()
    paginator=Paginator(shemas_list,9)
    num_page=request.GET.get('page')
    try:
        shemas=paginator.page(num_page)
    except EmptyPage:
        shemas=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        shemas=paginator.page(1)
    return render(request,'articles/shemas.html',{'shemas':shemas,'category_list':category_list,
                'subcat_name':subcat_name,'cat_name':cat_name,'cat_id':cat_id})

#Обработка формы запроса на проведение занятия
def GetLessonCreateView(request):
    form_getlesson=LessonForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form_getlesson=LessonForm(request.POST)
        if form_getlesson.is_valid():
            #сохраняем данные
            form_getlesson.save()
            #формируем письмо для уведомления
            client=request.POST.__getitem__('Person_name')
            subj_num=request.POST.__getitem__('lesson_category')
            subj=Category.objects.get(id=int(subj_num))

            phone=request.POST.__getitem__('Person_phone')
            email=request.POST.__getitem__('Person_email')
            date=datetime.datetime.strptime(request.POST.__getitem__('lesson_date'),"%Y-%m-%d")
            date_f=date.strftime('%d-%m-%Y')
            comment=request.POST.__getitem__('comments')

            message_template='Поступила новая заявка на занятие! \n Клиент:{cl_name}  \n Предмет:{subject} \n Хочет начать заниматься:{d} \
            \n\nТелефон:{tel} \n Почта:{em} \n Комментарий от клиента:\n\t{com} '
            message=message_template.format(cl_name=client,subject=subj,d=date_f,tel=phone,em=email,com=comment)
            send_mail('Новый запрос на занятие', message, settings.EMAIL_HOST_USER, ['Na5tyu5ha@mail.ru'],fail_silently=True)
            return redirect('success_lesson')

    d = datetime.date.today()

    c = EventCalendar(locale='')
    html_calendar = c.formatmonth(d.year, d.month, withyear=True)
    #html_calendar = html_calendar.replace('<td ', '<td  width="35px" height="35px"')
    month_num=d.month;

    return render(request,'articles/getlesson.html',{'form':form_getlesson,'html_calendar':html_calendar,'month_num':month_num})

#обработчик ajax на смену месяца в календаре
def MonthChanger(request):
    if request.method == 'GET':
        month_num = int(request.GET['month_number'])
    nowday = datetime.date.today()
    d = EventCalendar(locale='')
    html_out = d.formatmonth(nowday.year, month_num)
    html_out = html_out.replace('<td ', '<td  width="35" height="35"')

    return HttpResponse(html_out)



#конспекты, рабочие программы
def ShowConspects(request,cat_id):
    category_list=Category.objects.all()
    try:
        Conspect_list=Conspect.objects.all().filter(cons_category=cat_id)
    except:
        Conspect_list=None
    return render(request,'articles/Conspects.html',{'Conspect_list':Conspect_list,'category_list':category_list,})


def ShowTeacherLS(request,cat_id):
    category_list=Category.objects.all()
    try:
        Workpr_list=LiterSource.objects.all().filter(lit_category=cat_id)

        paginator=Paginator(Workpr_list,6)

        num_page=request.GET.get('page')
        try:
            books=paginator.page(num_page)
        except EmptyPage:
            books=paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            books=paginator.page(1)
    except:
        Workpr_list=None
    return render(request,'articles/TeacherLS.html',{'Workpr_list':Workpr_list,'category_list':category_list,'books':books})

#чек-листы
def ShowCheckLists(request,direct_id='1'):
    current_dir=Direction_CHL.objects.get(id=direct_id)
    qty_dir=Direction_CHL.objects.count()
    try:
        chl_list=CHeckList.objects.filter(chl_direct=direct_id)
    except:
        chl_list=None
    return render(request,'articles/CheckLists.html',{'chl_list':chl_list,'current_dir':current_dir,'qty_dir':qty_dir})

def ShowCheckLists2(request):
    pass

#онлаqн-тесты и их проверка
def OnlineTestList(request,direct_id='1'):

    category_list=Category.objects.all()
    direction_list=Direction.objects.all()
    try:
        direction_list=Direction.objects.all().order_by('id')
    except:
        direction_list=None

    category_test_list=[0]
    for category in category_list:
        test_list=OnlineTest.objects.all().filter(test_direct=direct_id,test_category=category.id)
        category_test_list.append(test_list)
    #формируем данные об уже пройденых тестах
    if request.user.is_authenticated:
        all_tests=OnlineTest.objects.filter(test_direct=direct_id)
        all_tests_ids=[]

        for t in all_tests:
            all_tests_ids.append(t.id)
        uniq_allt_ids=set(all_tests_ids)

        alltest_att_dict={}
        alltest_att_dict=dict.fromkeys(uniq_allt_ids)

        for k in alltest_att_dict.keys():
            #смотрим максимальное количество возможных попыток в тесте
            cur_test=OnlineTest.objects.get(id=k)
            total_test_attempts=int(cur_test.max_attempts)
            #смотрим самую позднюю из существующих попыток
            exist_atmpts=Test_result.objects.filter(test=cur_test,tested_user=request.user)
            exist_atmpts_list=[]
            for a in exist_atmpts:
                exist_atmpts_list.append(int(a.attempt_number))
            if len(exist_atmpts_list)>0:
                last_attempt=max(exist_atmpts_list)
            else:
                last_attempt=0
            alltest_att_dict[k]=total_test_attempts-last_attempt
    else:
        alltest_att_dict={}

    return render(request,'articles/testlist.html',{'category_list':category_list,'direction_list':direction_list,
    'category_test_list':category_test_list,'alltest_att_dict':alltest_att_dict})

#регистрация пользователей
def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
       new_user=form.save(commit=False)
       new_user.save()
       return render(request, 'articles/register_done.html', {'new_user': new_user})
  else:
    form = SignUpForm()
  return render(request, 'articles/signup.html', {'form': form})




@login_required
def PassTest(request,test_id):
    context=generate_context_for_test_by_testid(test_id)

    if request.method == 'POST':
        total_points=0
        student_points=0
        quest_with_points={}
        dict=request.POST.dict()
        keys=dict.keys()
        answers=list(dict)
        answers.remove('csrfmiddlewaretoken')

        #расчет общего количества баллов за вопрос, вес в баллах за один правильный ответ, количество набранных баллов
        if len(keys)>1:
            quest_list=[]
            for k in keys:
                if k!='csrfmiddlewaretoken':
                    ans=Answer.objects.get(id=int(k))
                    q0=ans.question
                    q1=q0.id
                    if q1 not in quest_list:
                        quest_list.append(q1)

            for q in quest_list:
                quest=TestQuestion.objects.get(id=q)
                right_answers=Answer.objects.filter(question=quest,iscorrect='Y')
                right_answer_qty=len(right_answers)
                total_points+=quest.points
                points_per_answer=quest.points/right_answer_qty
                quest_with_points[q]=points_per_answer



            for k in keys:
                if k!='csrfmiddlewaretoken':
                    answer=Answer.objects.get(id=k)
                    quest=answer.question
                    if answer.iscorrect=='Y':
                        points=int(quest_with_points[quest.id])
                        student_points+=points

            #связка с нужным тестом
            link_quest=TestQuestion.objects.get(id=int(quest_list[0]))
            test0=link_quest.test
            test_id=test0.id
            test1=OnlineTest.objects.get(id=test_id)
            test_quests=TestQuestion.objects.filter(test=test1)
            test_quest_qty=len(test_quests)
            fact_qty=int(len(quest_list))

            percent=round(student_points/total_points*100,2)

            error_quest_qty=0

            if (test_quest_qty > fact_qty):
                percent=0
                total_points=0
                student_points=0
                error_quest_qty=1

            all_test_quest=[]
            for q in test_quests:
                all_test_quest.append(q.id)
            unansw_quest=list(set(all_test_quest)-set(quest_list))

            #записываем результат прохождения для зарегистрированных пользователе
                #вычисляем число попыток
            total_attempts=test1.max_attempts
            list_results=Test_result.objects.filter(tested_user=request.user,test=test1)
            existing_atm=len(list_results)+1

            error_attempts=0
            if (existing_atm > total_attempts):
                error_attempts=1


                #сохраняем результат ()
            if (error_attempts==0 and error_quest_qty==0):
                tr=Test_result()
                tr.tested_user=request.user
                tr.t_user_name=request.user.first_name
                tr.t_user_surname=request.user.last_name
                if len(request.user.groups.all())>0:
                    tr.t_user_group=request.user.groups.all()[0]
                tr.test=test1
                tr.test_category=test1.test_category
                tr.test_direction=test1.test_direct
                tr.test_data=datetime.date.today()
                tr.attempt_number=existing_atm
                tr.result_points=student_points
                tr.test_points=total_points
                tr.result_percentage=percent
                tr.save()

                #сохраняем детально ответы
                for ans in answers:
                    answer_obj=Answer.objects.get(id=ans)
                    useranswer=AnswerRecieved()
                    useranswer.result=tr
                    useranswer.answer=answer_obj
                    useranswer.isright=answer_obj.iscorrect
                    useranswer.save()


            passed_test_context={'unansw_quest':unansw_quest,'answers':answers,
            'total_points':total_points,'student_points':student_points,'percent':percent,
            'error_quest_qty':error_quest_qty,'existing_atm':existing_atm,'total_attempts':total_attempts,'error_attempts':error_attempts}
            context.update(passed_test_context)




            return render(request,'articles/test.html',context)



    return render(request,'articles/test.html',context)
