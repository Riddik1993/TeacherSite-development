from django.db import models
from datetime import datetime
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.contrib.auth.models import User,Group

#памятки по истории и обществознанию
class MemSocial_Article(models.Model):
    article_title=models.CharField('название статьи',max_length=200)
    article_description=models.TextField('Краткая информация',blank=True)
    article_text=models.TextField('текст статьи')
    pub_date=models.DateTimeField('дата публикации',auto_now_add=True)
    file=models.FileField(upload_to='socialdocs/',blank=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name='Памятка по обществознанию'
        verbose_name_plural='Памятки по обществознанию'

class Test_result(models.Model):
    tested_user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь', related_name="tested_user")
    t_user_name=models.CharField('имя',max_length=200,null=True)
    t_user_surname=models.CharField('Фамилия',max_length=200,null=True)
    t_user_group=models.ForeignKey(Group,on_delete=models.PROTECT,verbose_name='Группа', blank=True,null=True,related_name="t_user_group")
    test=models.ForeignKey('OnlineTest',on_delete=models.CASCADE,verbose_name='Тест')
    test_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет теста')
    test_direction=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление теста')
    test_data=models.DateTimeField('дата прохождения')
    attempt_number=models.IntegerField('Номер попытки')
    result_points=models.FloatField('Набранные баллы')
    test_points=models.FloatField('Максим.баллы в тесте')
    result_percentage=models.FloatField('Результат в процентах')

    def __str__(self):
       return self.test.test_name

    class Meta:
        verbose_name='Результат теста'
        verbose_name_plural='Результаты тестов'


class Memhis_Article(models.Model):
    article_title=models.CharField('название статьи', max_length=200)
    article_description=models.TextField('Краткая информация',blank=True)
    article_text=models.TextField('текст статьи')
    pub_date=models.DateTimeField('дата публикации',auto_now_add=True)
    file=models.FileField(upload_to='historydocs/',blank=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name='Памятка по истории'
        verbose_name_plural='Памятки по истории'
#информация о себе
class SelfInfo(models.Model):
    article_title=models.CharField('Название статьи',max_length=200)
    article_text=models.TextField('текст статьи')
    image=models.ImageField(upload_to='images/',blank=True)
    image2=models.ImageField(upload_to='images/',blank=True)
    image3=models.ImageField(upload_to='images/',blank=True)
    image4=models.ImageField(upload_to='images/',blank=True)
    image5=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name='Информация о себе'
        verbose_name_plural='Информация о себе'
#информация на главной странице
class MainInfo(models.Model):
    article_title=models.CharField('Название статьи',max_length=200)
    article_text=models.TextField('текст статьи')
    article_text2=models.TextField('текст статьи2',default="text")
    signature=models.TextField('Подпись',max_length=100,default=" ")
    image=models.ImageField(upload_to='images/',blank=True)
    image2=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
      return self.article_title

    class Meta:
        verbose_name='Информация на главной странице'
        verbose_name_plural='Информация на главной странице'


#таблицы и схемы

class Shema(models.Model):
    shema_title=models.CharField('Название_схемы',max_length=200)
    shema_description=models.TextField('Краткое описание',max_length=400)
    shema_category=models.ForeignKey('Category',null=True,on_delete=models.PROTECT,verbose_name='Категория схемы')
    schema_subcategory=models.ForeignKey('Schema_subcategory',null=True,blank=True,on_delete=models.PROTECT,verbose_name='Подкатегория схемы')
    shema_image=models.ImageField(upload_to='images/shemas',blank=True)
    pub_date=models.DateTimeField('дата публикации',blank=True,auto_now_add=True)
    def __str__(self):
        return self.shema_title

    class Meta:
        verbose_name='Схема'
        verbose_name_plural='Схемы'

class Category(models.Model):
    category_name=models.CharField('Предмет',max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name='Предмет'
        verbose_name_plural='Предметы'


#Направления подготовки
class Direction(models.Model):
    direction_name=models.CharField('Направление',max_length=100)

    def __str__(self):
        return self.direction_name

    class Meta:
        verbose_name='Направление подготовки'
        verbose_name_plural='Направления подготовки'

#запись на занятие
class Lesson(models.Model):
    Person_name=models.CharField('Имя',max_length=100)
    lesson_category=models.ForeignKey('Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет урока')
    Person_phone=models.CharField('Номер телефона',max_length=100)
    Person_email=models.EmailField('Email',max_length=100)
    lesson_date=models.DateField('Дата занятия',null=True)
    comments=models.TextField('Комментарии',max_length=250,null=True)

    def __str__(self):
        return self.Person_name

    class Meta:
        verbose_name='Заявки на занятие'
        verbose_name_plural='Заявки на занятие'

# комментарии
class ArticleComment(models.Model):
    Person_name=models.CharField('Имя',max_length=100)
    Person_email=models.EmailField('Email',max_length=100)
    comments=models.TextField('Комментарий',max_length=250,null=True)
    Article=models.ForeignKey('Memhis_Article',on_delete=models.CASCADE)
    pub_date=models.DateTimeField('дата комментария',null=True,auto_now_add=True)
    publish_choices=[('Y','Да'),('N','Нет')]
    publish=models.CharField('Публиковать?',max_length=3,choices=publish_choices,default='N')
    def __str__(self):
        return self.comments

    class Meta:
        verbose_name='Комментарии к статьям по истории'
        verbose_name_plural='Комментарии к статьям по истории'

#события календаря
class Event(models.Model):
    day = models.DateField('Свободный день для занятий', help_text='Свободный день для занятий')
    notes = models.TextField('Комментарий', help_text='Комментарий', blank=True, null=True)
    BUSY_CHOICES=[('FREE','Свободен'),('BUSY','Занят'),('NO_ACT','Не занимаюсь')]

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name = 'Свободный день для занятий'
        verbose_name_plural = 'Свободные дни для занятий'

#конспекты
class Conspect(models.Model):
        cons_name=models.CharField('название конспекта', max_length=200)
        cons_descr=models.CharField('описание конспекта', max_length=500)
        cons_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
        file=models.FileField(upload_to='conspects/',blank=True)
        cons_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')
        pub_date=models.DateTimeField('дата публикации',blank=True,auto_now_add=True)
        def __str__(self):
            return self.cons_name

        class Meta:
            verbose_name='Конспект'
            verbose_name_plural='Конспекты'

#рабочие программы
class LiterSource(models.Model):
        lit_name=models.CharField('название', max_length=200)
        lit_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
        file=models.FileField(upload_to='workprograms/',blank=True)
        lit_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')
        pub_date=models.DateTimeField('дата публикации',blank=True,auto_now_add=True)

        def __str__(self):
            return self.lit_name
        class Meta:
            verbose_name='Литература'
            verbose_name_plural='Литература'
#чек-листы
class CHeckList(models.Model):
    chl_name=models.CharField('название', max_length=200)
    chl_descr=models.CharField('описание', max_length=500)
    chl_direct=models.ForeignKey('articles.Direction_CHL',null=True,on_delete=models.PROTECT,verbose_name='Направление чек-листа')
    pub_date=models.DateTimeField('дата публикации',blank=True,auto_now_add=True)
    file=models.FileField(upload_to='checklists/',blank=True)

    def __str__(self):
        return self.chl_name

    class Meta:
        verbose_name='CHECK-лист'
        verbose_name_plural='CHECK-листы'

class Direction_CHL(models.Model):
    direction_name=models.CharField('Направление чек-листа',max_length=100)

    def __str__(self):
        return self.direction_name

    class Meta:
        verbose_name='Направление чек-листов'
        verbose_name_plural='Направления чек-листов'




#онлайн тесты
class OnlineTest(models.Model):
    test_name=models.CharField('название', max_length=200)
    test_descr=models.CharField('описание', max_length=500)
    test_direct=models.ForeignKey('articles.Direction',null=True,on_delete=models.PROTECT,verbose_name='Направление')
    test_category=models.ForeignKey('articles.Category',null=True,on_delete=models.PROTECT,verbose_name='Предмет')
    pub_date=models.DateTimeField('дата публикации',blank=True,auto_now_add=True)
    max_attempts=models.IntegerField(default=2,verbose_name='Число попыток')


    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name='Онлайн-тест'
        verbose_name_plural='Онлайн-тесты'


class TestQuestion(models.Model):
    question=models.CharField('вопрос', max_length=400)
    test=models.ForeignKey('articles.OnlineTest',null=True,on_delete=models.CASCADE,verbose_name='тест')
    points=models.IntegerField('Количество баллов',validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.question

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

class Answer(models.Model):
    answer=models.CharField('Ответ', max_length=400)
    question=models.ForeignKey('articles.TestQuestion',null=True,on_delete=models.CASCADE,verbose_name='вопрос')
    correct_choices=[('Y','Да'),('N','Нет')]
    iscorrect=models.CharField('правильный?',max_length=3,choices=correct_choices,default='N')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name='Ответ'
        verbose_name_plural='Ответы'


class MP_new(models.Model):
    new_title=models.CharField('Название новости',max_length=200)
    new_description=models.TextField('Описание',max_length=800)
    new_image=models.ImageField(upload_to='images/news',blank=True)

    def __str__(self):
        return self.new_title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'

class Schema_subcategory(models.Model):
    category=models.ForeignKey('articles.Category',null=False,on_delete=models.CASCADE,verbose_name='Предмет')
    subcategory_name=models.CharField('Название_подкатегории',max_length=100)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name='Подкатегория схем'
        verbose_name_plural='Подкатегории схем'
