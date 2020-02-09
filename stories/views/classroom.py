from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext
from ..models import Cases, Student, User, School
from  stories.filters import CasesFilter


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:stories_list')
        else:
            return redirect('students:students_borad')
    return render(request, 'classroom/home.html')


    
def Introduction(request):
     template_name = 'classroom/Introduction.html'
     return render(request, template_name)



def Research(request):
     case_list = Cases.objects.all()
     case_filter = CasesFilter(request.GET, queryset = case_list)
     template_name = 'classroom/research.html'
     return render(request, template_name, {'filter' : case_filter})



def Stories(request):
     posts = Cases.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
     return render(request, 'classroom/stories.html', {'posts':posts})



