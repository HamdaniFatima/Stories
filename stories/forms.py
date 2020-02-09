from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from stories.models import (Cases, School, Student, User, Teacher, Comment, Storie, Case_publ)
from django.forms import ModelChoiceField
from django.forms import ModelMultipleChoiceField
from django.forms import ModelForm
from django.utils.translation import ugettext



class TeacherSignUpForm(UserCreationForm):
    
    
    Schools = forms.ModelMultipleChoiceField(
        queryset=School.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
   
 
    class Meta(UserCreationForm.Meta):
        model = User
      
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.school.add(*self.cleaned_data.get('Schools'))
        return user


class StudentSignUpForm(UserCreationForm):
    Schools = forms.ModelMultipleChoiceField(
        queryset=School.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.school.add(*self.cleaned_data.get('Schools'))
        return user


class GroupForm(ModelForm):
    class Meta:
       model = Cases
       fields = ['title_case', 'subject', 'produit', 'context', 'description', 'description_shema', 'processus']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title_comment', 'state_comment', 'produit_comment', 'context_comment', 'description_comment', 'diagnostic_comment', 'processus_comment', 'references_comment', 'abstract_comment',  'general_remarks'   )


class StorieForm(forms.ModelForm):

    class Meta:
        model = Storie
        fields = ['story']
      
      

class pubForm(forms.ModelForm):

    class Meta:
       model = Case_publ
       fields = ['publish_date']