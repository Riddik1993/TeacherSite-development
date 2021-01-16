from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('MemSocial/',views.MemSocialList,name='MemSocialList'),
    path('MemSocial/<int:article_id>/',views.MemSocialDetail,name='MemSocialDetail'),
    path('MemHistory/',views.MemHistory,name='MemHistory'),
    path('MemHistory/<int:article_id>/',views.MemHistoryDetail,name='MemHistoryDetail'),
    path('about/',views.About,name='SelfInfo'),
    path('',views.ShowMainInfo,name='main'),
    path('literature/',views.ShowLiteratureList,name='literature'),
    path('shemas/<int:cat_id>/',views.ShowShemasSubcat,name='shemas_subcat'),
    path('shemas/<int:cat_id>/<int:subcat_id>',views.ShowShemas,name='shemas'),
    path('getlesson/',views.GetLessonCreateView,name='getlesson'),
    path('getlesson/monthch',views.MonthChanger,name='MonthChanger'),
    path('successlesson/',TemplateView.as_view(template_name='articles/success_lesson.html'),name='success_lesson'),
    path('successcomment/',TemplateView.as_view(template_name='articles/success_comment.html'),name='success_comment'),
    path('conspects/<int:cat_id>/',views.ShowConspects,name='conspects'),
    path('teacherls/<int:cat_id>/',views.ShowTeacherLS,name='teacherls'),
    path('chlists/<int:direct_id>/',views.ShowCheckLists,name='chlists'),
    path('chlists/',views.ShowCheckLists2,name='chlists2'),
    path('onlinetests/<int:direct_id>',views.OnlineTestList,name='tests'),
    path('vpr/',views.ShowVpr,name='vpr'),
    path('test/<int:test_id>',views.PassTest,name='GoTest'),
    path('achievelist/',views.SendAchievListJSON,name='achieve_list'),
    path('achievements/',views.ShowAchievements,name='achievements'),
    path('ach_info/',views.ShowAchInfo,name='achiev_info')
    



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
