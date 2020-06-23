from django.db import models
from  datetime import datetime
from django.utils import timezone
from articles.models import Category,Direction

class ExamInfo(models.Model):
    exam_name=models.CharField('название экзамена', max_length=150)
    exam_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
    exam_descr=models.CharField('описание экзамена', max_length=300)
    file=models.FileField(upload_to='examdocs/examinfo',blank=True)
    exam_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name='Информация об экзаменах'
        verbose_name_plural='Информация об экзаменах'

class LiteratureList(models.Model):
    lit_name=models.CharField('название списка', max_length=150)
    lit_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
    file=models.FileField(upload_to='examdocs/literaturelist',blank=True)
    lit_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')

    def __str__(self):
        return self.lit_name

    class Meta:
        verbose_name='Список литературы'
        verbose_name_plural='Список литературы'


class Task(models.Model):
        task_name=models.CharField('название задания', max_length=200)
        task_descr=models.CharField('описание задания', max_length=300)
        task_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
        file=models.FileField(upload_to='examdocs/tasks',blank=True)
        task_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')
        pub_date=models.DateTimeField('дата публикации',blank=True,default=datetime.now())
        def __str__(self):
            return self.task_name

        class Meta:
            verbose_name='Задание'
            verbose_name_plural='Задания'

# отзывы

class FeedBack(models.Model):
    Person_name=models.CharField('Имя',max_length=100)
    Person_email=models.EmailField('Email',max_length=100)
    comments=models.TextField('Комментарий',max_length=400)
    pub_date=models.DateTimeField('дата отзыва',auto_now_add=True)
    publish_choices=[('Y','Да'),('N','Нет')]
    publish=models.CharField('Публиковать?',max_length=3,choices=publish_choices,default='N')

    def __str__(self):
        return self.comments

    class Meta:
        verbose_name='Отзывы'
        verbose_name_plural='Отзывы'



# Create your models here.
