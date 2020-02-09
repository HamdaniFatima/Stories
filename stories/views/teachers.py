from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorators import teacher_required
from ..models import Cases, Teacher, School, User,  Comment, SummaryHistory, Case_publ
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from ..forms import  TeacherSignUpForm, CommentForm, StorieForm, pubForm
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.utils.translation import ugettext
from django.shortcuts import render
from django.http import HttpResponseRedirect



class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form_teacher.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:stories_list')



@method_decorator([login_required, teacher_required], name='dispatch')
class TeachersListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/teachers/board/index.html'


    

@method_decorator([login_required, teacher_required], name='dispatch')
class TermsListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/teachers/board/terms_teacher.html'





@method_decorator([login_required, teacher_required], name='dispatch')
class TableListView(ListView):
    model = Cases
    ordering = ('title_case', )
    context_object_name = 'cases'
    template_name = 'classroom/teachers/board/tables-basic.html'

    def get_queryset(self):
        teacher = self.request.user.teacher
        teacher_schools = teacher.school.values_list('pk', flat=True)
        # taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Cases.objects.filter(school_case__in = teacher_schools) 
        return queryset





@login_required
@teacher_required
def publication(request, pk):
    quiz = get_object_or_404(Cases, pk=pk)
    teacher = request.user.teacher
    template_name = 'registration/signup_form_teacher.html'


    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.case= quiz
            post.save()
            return redirect('teachers:take_quiz', quiz.pk)
  


def EvaluerlistView(request, pk):
    try:
        comment = get_object_or_404(Comment, pk=pk)
    except Comment.DoesNotExist:
            raise Http404('cases does not exist')

    return render(request, 'classroom/teachers/board/takens.html', {'comment': comment}  )


@login_required
@teacher_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Cases, pk=pk)
    teacher = request.user.teacher
    template_name = 'registration/signup_form_teacher.html'

    try:

        summary_history = SummaryHistory.objects.filter(case__pk= quiz.pk).order_by('-version')
    except summary_history.DoesNotExist:
            raise Http404('cases does not exist')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.case= quiz
            post.owner = request.user
            post.save()
            return redirect('teachers:take_quiz', quiz.pk)
    else:

        form = CommentForm()
        try:
            quiz = get_object_or_404(Cases, pk=pk)
            Comments = Comment.objects.filter(case__pk= quiz.pk).order_by('date_comment')
        except Comment.DoesNotExist:
               raise Http404('cases does not exist')

    return render(request, 'classroom/teachers/board/forms.html', {'form': form, 'quiz':quiz, 'Comments': Comments, 'summary_history': summary_history})




@login_required
@teacher_required
def modifaction(request, pk):
    try:
        quiz = get_object_or_404(Cases, pk=pk)
        summary_history = SummaryHistory.objects.filter(case__pk= quiz.pk).order_by('-version')
    except summary_history.DoesNotExist:
            raise Http404('cases does not exist')

    return render(request, 'classroom/teachers/board/tables-basic.html', {'summary_history': summary_history}  )



@method_decorator([login_required, teacher_required], name='dispatch')
class DatesListView(ListView):
    model = School
    context_object_name = 'cases'
    template_name ='classroom/teachers/board/dates.html'
    
    def get_queryset(self):
        queryset = self.request.user.teacher.school\
            .prefetch_related('teacher_school') 
        return queryset






@login_required
@teacher_required
def publi_quiz(request, pk):
    quiz = get_object_or_404(Cases, pk=pk)
    
    try:
           newSummary = Case_publ(case_publ=quiz)
           newSummary.save()
    except quiz.DoesNotExist:
            raise Http404('cases does not exist')

    return render(request, 'classroom/teachers/board/index.html' )




@method_decorator([login_required, teacher_required], name ='dispatch')
class QuizDeleteView(DeleteView):
    model = Cases
    context_object_name = 'case'
    template_name = 'classroom/teachers/case_delete_confirm.html'
    success_url = reverse_lazy('teachers:table_list')

    def delete(self, request, *args, **kwargs):
        quiz = self.get_object()
        messages.success(request, 'The quiz %s was deleted with success!' % quiz.title_case)
        return super().delete(request, *args, **kwargs)

    

           


    





