from django.urls import include, path
from .views import classroom, students, teachers



urlpatterns = [
    path('', classroom.home, name='home'),
    path('Innovtion/', classroom.Introduction, name='Introduction'),
    path('Stories/', classroom.Stories, name='Stories'),
    path('Research/', classroom.Research, name='Research'),
    path('teachers/', include(([
        path('', teachers.TeachersListView.as_view(), name='stories_list'),
        path('studies/tables/', teachers.TableListView.as_view(), name='table_list'),
        path('comments/<int:pk>/', teachers.EvaluerlistView, name='comment_list'),
        path('case/<int:pk>/', teachers.take_quiz, name='take_quiz'),
         path('case/Remove/<int:pk>/', teachers.QuizDeleteView.as_view(), name='delete_quiz'),
        path('story/<int:pk>/', teachers.publi_quiz, name='publi_quiz'),
        path('studies/', teachers.modifaction, name='modif_quiz'),
        path('board/terms/', teachers.TermsListView.as_view(), name='terms_teacher_list'),
       
   
        

        
#<int:pk>/

    ], 'stories'), namespace='teachers')),

   path('students/', include(([    
        path('', students.HomeListView.as_view(), name='students_home'),
        path('board/', students.StudiesListView.as_view(), name='students_borad'),
        path('board/contenu', students.contenuListView.as_view(), name='students_contenu'),
        path('board/enjeu', students.enjeuListView.as_view(), name='students_enjeu'),
        path('board/comite', students.comiteListView.as_view(), name='students_comite'),
        path('board/exemple', students.exempleListView.as_view(), name='students_exemple'),
        path('board/tables/', students.TableListView.as_view(), name='table_list'),
        path('board/dates/', students.DatesListView.as_view(), name='dates_list'),
        path('board/information/', students.InfoListView.as_view(), name='info_list'),
        path('board/terms/', students.TermsListView.as_view(), name='terms_list'),
        path('case/add/', students.CaseCreateView.as_view(), name='case_add'),
        path('case/<int:pk>/change', students.CaseUpdateView.as_view(), name='case_change'),
        path('case/<int:pk>/delete/', students.QuizDeleteView.as_view(), name='case_delete'),
        path('case/<int:pk>/display', students.post_detail, name='post_detail'),
        path('case/<int:pk>/evaluation', students.evaluation_quiz, name='evalu_detail'),
        ], 'stories'), namespace='students')),

]

