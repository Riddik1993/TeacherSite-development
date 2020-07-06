from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import MemSocial_Article,Memhis_Article,SelfInfo,MainInfo,Shema,Category,Lesson,ArticleComment,Direction,Event,Conspect,\
LiterSource,CHeckList,Direction_CHL,OnlineTest,TestQuestion,Answer,Test_result,MP_new,Schema_subcategory

# класс, позволяющий вкладывать ссылки в админке на форму другой модели
class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}">Редактировать</a>'.format(u=url))
        else:
            return ''



class EventAdmin(admin.ModelAdmin):
    list_display=('day','notes')

class ShemaAdmin(admin.ModelAdmin):
    list_display=('shema_title','shema_category','schema_subcategory','shema_description')
    list_display_links=('shema_title',)
    list_filter=('shema_category','schema_subcategory')
    search_fields=('shema_title','shema_category')

class LessonAdmin(admin.ModelAdmin):
    list_display=('Person_name','lesson_category','comments')
    list_display_links=('Person_name',)
    list_filter=('lesson_category',)
    search_fields=('Person_name','comments')

class ConspectAdmin(admin.ModelAdmin):
    list_display=('cons_name','cons_descr','cons_direct','pub_date',)
    list_display_links=('cons_name',)
    list_filter=('cons_category','cons_direct',)
    search_fields=('cons_name',)

class LiterSourceAdmin(admin.ModelAdmin):
    list_display=('lit_name','lit_direct','pub_date',)
    list_display_links=('lit_name',)
    list_filter=('lit_category','lit_direct',)
    search_fields=('lit_name',)

class CHeckListAdmin(admin.ModelAdmin):
    list_display=('chl_name','chl_descr','chl_direct','pub_date',)
    list_display_links=('chl_name',)
    list_filter=('chl_direct',)
    search_fields=('chl_name',)

#тест и вложенные вопросы

class TestQuestionLinkInline(EditLinkToInlineObject, admin.TabularInline):
    model = TestQuestion
    fields = ('question','points', 'edit_link',)
    readonly_fields = ('edit_link',)

class OnlineTestAdmin(admin.ModelAdmin):
    list_display=('test_name','test_descr','test_direct','test_category','pub_date',)
    list_display_links=('test_name',)
    list_filter=('test_direct','test_category')
    inlines=[TestQuestionLinkInline]
    search_fields=('test_name','test_descr')

#вопрос и вложенные ответы
class AnswerInline(admin.TabularInline):
    model = Answer


class TestQuestionAdmin(admin.ModelAdmin):
    list_display=('question','test','points')
    list_display_links=('question',)
    list_filter=('test',)
    inlines=[AnswerInline]
    search_fields=('question',)

#результаты тестов по юзерам
class Test_resultAdmin(admin.ModelAdmin):
    list_display=('t_user_name','t_user_surname','t_user_group','test','test_data','result_percentage','attempt_number')
    list_display_links=('t_user_name',)
    list_filter=('t_user_group','test_category','test','test_direction','t_user_surname')
    search_fields=('tested_user','test')
#новости
class MP_newAdmin(admin.ModelAdmin):
    list_display=('new_title','new_description')
    list_display_links=('new_title','new_description')
    search_fields=('new_title','new_description')
#подкатегории схем
class Schema_subcategoryAdmin(admin.ModelAdmin):
    list_display=('category','subcategory_name')
    list_filter=('category',)
    list_display_links=('category','subcategory_name')



admin.site.register(MemSocial_Article)
admin.site.register(Memhis_Article)
admin.site.register(SelfInfo)
admin.site.register(MainInfo)
admin.site.register(Shema,ShemaAdmin)
admin.site.register(Category)
admin.site.register(Direction_CHL)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(ArticleComment)
admin.site.register(Direction)
admin.site.register(Event,EventAdmin)
admin.site.register(Conspect,ConspectAdmin)
admin.site.register(LiterSource,LiterSourceAdmin)
admin.site.register(CHeckList,CHeckListAdmin)
admin.site.register(OnlineTest,OnlineTestAdmin)
admin.site.register(TestQuestion,TestQuestionAdmin)
admin.site.register(Test_result,Test_resultAdmin)
admin.site.register(MP_new,MP_newAdmin)
admin.site.register(Schema_subcategory,Schema_subcategoryAdmin)
