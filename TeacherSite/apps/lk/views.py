from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from articles.models import Test_result
#памятки по истории и обществознанию
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
    results=Test_result.objects.filter(tested_user=request.user)

    return render(request,'lk/mytests.html',{'results':results})

@login_required
def Show_LK_Favor(request):
    return render(request,'lk/myfavor.html')


# Create your views here.
