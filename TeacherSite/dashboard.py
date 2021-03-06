"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'TeacherSite 24032020.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name



class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"

        self.children.append(modules.ModelList(
                    title='Информация для учеников',
                    column=1,
                    models=('articles.models.MemSocial_Article','articles.models.Memhis_Article','articles.models.Shema','mainapp.models.ExamInfo',
                    'mainapp.models.LiteratureList','mainapp.models.Task','articles.models.OnlineTest','articles.models.Test_result',
                    'articles.models.VPR')
                 )

        )

        self.children.append(modules.ModelList(
                    title='Информация для учителей',
                    column=2,
                    models=('articles.models.Conspect','articles.models.LiterSource','articles.models.CHeckList')
                )

        )
        self.children.append(modules.ModelList(
                    title='Мое расписание',
                    column=1,
                    models=('articles.models.Event','articles.models.Lesson',)
                )

        )
        self.children.append(modules.ModelList(
                    title='Обратная связь',
                    column=1,
                    models=('articles.models.ArticleComment','mainapp.models.FeedBack',)
                )

        )

        self.children.append(modules.ModelList(
            _('Управление сайтом'),
            column=3,
            collapsible=False,
            models=('django.contrib.*',),
        ))
        self.children.append(modules.ModelList(
            _('Оформление'),
            column=3,
            collapsible=False,
            models=('articles.models.Img_reminder',),
        ))
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Классификация документов'),
            column=3,
            collapsible=False,
            models=('articles.models.Category','articles.models.Schema_subcategory',
            'articles.models.Direction','articles.models.Direction_CHL','articles.models.VPRtype'),
        ))
        self.children.append(modules.ModelList(
            _('Личная информация'),
            column=3,
            collapsible=True,
            models=('articles.models.MainInfo','articles.models.SelfInfo','articles.models.MP_new',
                    'articles.models.Achievement','articles.models.AchievementCategory'),
        ))
        self.children.append(modules.ModelList(
                _('Задачи по расписанию и отложенные'),
                column=3,
                collapsible=False,
                models=('django_q.models.*',),
            ))
        #ссылка на графики по использованию сервера
        self.children.append(modules.LinkList(
            title='Ресурсы сервера',
            column=2,
            children=(
                {
                    'title': 'Просмотреть состояние сервера',
                    'url': '/serverinfo',
                    'external': False,
                    'description': 'Проверьте свободную память и текущую нагрузку',
                    'target': '_blank',
                },
                            )
        ))



        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Последние действия'),
            limit=5,
            collapsible=False,
            column=3,
        ))
