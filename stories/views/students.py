from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from ..decorators import student_required
from ..forms import  StudentSignUpForm, GroupForm
from ..models import Cases, Student, User, School, Comment, SummaryHistory
from django.utils.translation import ugettext
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.http import Http404



class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/student_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:students_borad')



class HomeListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/index.html'

@method_decorator([login_required, student_required], name='dispatch')
class StudiesListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/index.html'



@method_decorator([login_required, student_required], name='dispatch')
class TableListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/tables-basic.html'

    def get_queryset(self):
        queryset = self.request.user.cases \
            .select_related('school_case') 
        return queryset


@method_decorator([login_required, student_required], name='dispatch')
class DatesListView(ListView):
    model = School
    context_object_name = 'cases'
    template_name ='classroom/students/board/dates.html'
    
    def get_queryset(self):
        queryset = self.request.user.student.school\
            .prefetch_related('students_school') 
        return queryset


@method_decorator([login_required, student_required], name='dispatch')
class InfoListView(ListView):
    model = School
    context_object_name = 'cases'
    template_name ='classroom/students/board/information.html'
    
 
@method_decorator([login_required, student_required], name='dispatch')
class TermsListView(ListView):
    model = School
    context_object_name = 'cases'
    template_name ='classroom/students/board/terms.html'



@method_decorator([login_required, student_required], name='dispatch')
class CaseCreateView(CreateView):
    model = Cases
    fields = ('title_case', 'subject',  'produit', 'mois', 'image_produit', 'date', 'context', 'context_images', 'description', 'description_shema',  'diagnostic',  'diagnostic_shema',  'processus',  'processus_shema',  'reference', 'abstract', 'auteur', 'school_case', 'terms_and_conditions')
    template_name = 'classroom/students/board/forms-basic.html'
    #case_add_form

    def form_valid(self, form):
        case = form.save(commit=False)
        case.owner = self.request.user
        case.save()
        return redirect('students:case_change', case.pk)


@method_decorator([login_required, student_required], name='dispatch')
class CaseUpdateView(UpdateView):
    model = Cases
    fields = fields = ('title_case', 'subject', 'produit', 'mois', 'image_produit', 'date', 'context', 'context_images', 'description', 'description_shema',  'diagnostic',  'diagnostic_shema',  'processus',  'processus_shema',  'reference', 'abstract', 'auteur', 'school_case', 'terms_and_conditions')
    context_object_name = 'case'
    template_name = 'classroom/students/case_change_form.html'
    
    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.user.cases.all()
 
    def form_valid(self, form):
        case = form.save(commit=False)
        case.update_date = timezone.now()
        case.save()
        return redirect('students:case_change', case.pk)


        



@method_decorator([login_required, student_required], name='dispatch')
class QuizDeleteView(DeleteView):
    model = Cases
    context_object_name = 'case'
    template_name = 'classroom/students/case_delete_confirm.html'
    success_url = reverse_lazy('students:table_list')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        messages.success(request, 'The quiz %s was deleted with success!' % quiz.title_case)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.cases.all()







def post_detail(request, pk):
    post = get_object_or_404(Cases, pk=pk)
    return render(request, 'classroom/home/landing.html', {'post': post})
    
    #return render(request, 'classroom/students/case_form_display.html', {'post': post})
    


@login_required
@student_required
def evaluation_quiz(request, pk):
    try:
        quiz = get_object_or_404(Cases, pk=pk)
        Comments = Comment.objects.filter(case__pk= quiz.pk).order_by('date_comment')
    except Comment.DoesNotExist:
            raise Http404('cases does not exist')

    return render(request, 'classroom/students/board/evaluation_resultat.html', {'Comments': Comments}  )



@method_decorator([login_required, student_required], name='dispatch')
class contenuListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/contenu.html'


@method_decorator([login_required, student_required], name='dispatch')
class enjeuListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/enjeu.html'



@method_decorator([login_required, student_required], name='dispatch')
class comiteListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/comite.html'




@method_decorator([login_required, student_required], name='dispatch')
class exempleListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/students/board/exemple.html'