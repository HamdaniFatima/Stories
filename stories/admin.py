from django.contrib import admin
from stories.models import School
from stories.models import Teacher
from stories.models import Student
from stories.models import Cases 
from stories.models import Subject
from stories.models import  Mois
from stories.models import  Comment
from stories.models import  Case_publ



# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Cases)
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Mois)
admin.site.register(Comment)
admin.site.register(Case_publ)