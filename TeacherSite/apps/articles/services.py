
from .models import MemSocial_Article,Memhis_Article,SelfInfo,MainInfo,Category,Shema,Lesson,ArticleComment,Event,\
Conspect,LiterSource,CHeckList,Direction_CHL,OnlineTest,Direction,TestQuestion,Answer,Test_result,MP_new,Schema_subcategory, \
Img_reminder

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
