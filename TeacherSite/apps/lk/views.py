from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from articles.models import Test_result,AnswerRecieved,OnlineTest
from articles.services import generate_context_for_test_by_testid,paginate
from django.contrib.admin.views.decorators import staff_member_required
import json

@login_required
def ShowProfile(request):
    if request.user.is_authenticated:
        f_name = request.user.first_name
        s_name = request.user.last_name
        email=request.user.email

        groups=request.user.groups.all()

    return render(request,'lk/profile.html',{'f_name':f_name ,'s_name':s_name,'email':email,'groups':groups})

@login_required
def Show_LK_Tests(request):
    u_results=Test_result.objects.filter(tested_user=request.user)
    #записываем результаты в json для диаграммы
    bad=0;
    good=0;
    excellent=0;
    for res in u_results:
        r=res.result_percentage
        print(r)
        if r<=30:
            bad+=1
        elif 30<r<=75:
            good+=1
        else:
            excellent+=1
    res_counter={'b':bad,'g':good,'e':excellent}
    #пагинация результатов
    results=paginate(request,u_results,7)
    return render(request,'lk/mytests.html',{'results':results,'res_counter':res_counter})

@login_required
def Show_LK_Favor(request):
    return render(request,'lk/myfavor.html')

@staff_member_required
def show_result_of_test_by_resultid(request,result_id):
    t_result=Test_result.objects.get(id=result_id)
    test=t_result.test
    test_context=generate_context_for_test_by_testid(test.id)

    received_answers=AnswerRecieved.objects.filter(result=t_result)
    recieved_answer_dict={}
    for a in received_answers:
        recieved_answer_dict.update({a.answer.id:a.isright})



    context={'result':t_result,'recieved_answer_dict':recieved_answer_dict}
    context.update(test_context)


    return render(request,'lk/passedtestresult.html',context)


# Create your views here.
