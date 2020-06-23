from django.contrib import admin
from .models import ExamInfo,LiteratureList,Task,FeedBack


class TaskAdmin(admin.ModelAdmin):
    list_display=('task_name','task_category','task_direct')
    list_display_links=('task_name',)
    list_filter=('task_category','task_direct')
    search_fields=('task_name','task_descr')

class ExamInfoAdmin(admin.ModelAdmin):
    list_display=('exam_name','exam_category','exam_direct')
    list_display_links=('exam_name',)
    list_filter=('exam_category',)

class LiteratureListAdmin(admin.ModelAdmin):
    list_display=('lit_name','lit_category','lit_direct')
    list_display_links=('lit_name',)
    list_filter=('lit_category',)

class FeedBackAdmin(admin.ModelAdmin):
    list_display=('Person_name','comments','pub_date')
    list_display_links=('Person_name',)



admin.site.register(ExamInfo,ExamInfoAdmin)
admin.site.register(LiteratureList,LiteratureListAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(FeedBack,FeedBackAdmin)

# Register your models here.
