from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.db import models
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.utils import timezone
from djrichtextfield.widgets import RichTextWidget
from djrichtextfield.models import RichTextField
from django.utils.translation import ugettext_lazy 










State_CHOICES = (
    ('green','GREEN', ),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)


# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class School(models.Model):
    name_school = models.CharField(max_length=30, unique=True)
    adresse_school= models.CharField(max_length=90)
    speciality_school=models.CharField(max_length=30)
    email = models.EmailField()
    premier_stop = models.TextField(max_length=200, null=True, blank=True)
    deuxieme_stop = models.TextField(max_length=200, null=True, blank=True)
    limit_stop = models.TextField(max_length=200, null=True, blank=True )
    date_premier_stop = models.DateTimeField(null=True, blank=True)
    date_deuxieme_stop = models.DateTimeField(null=True, blank=True)
    date_limit_stop = models.DateTimeField(null=True, blank=True )
    color = models.CharField(max_length=7, default='#007bff')


    def __str__(self):
        return self.name_school

    def get_html_badge(self):
        name = escape(self.name_school)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)




class Teacher(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=70,blank=True)
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)
    school=models.ManyToManyField(School , related_name='teachers_schools')

   
    def __str__(self):
        return self.user.username





class Mois(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Cases(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')
    school_case = models.ForeignKey(School, on_delete=models.CASCADE,verbose_name=u"Sélectionnez votre Etablissement",  related_name='cases')
    mois = models.ForeignKey(Mois, on_delete=models.CASCADE,verbose_name=u"Month", related_name='cases_mois')
    # General Informations
    title_case = models.CharField(max_length=255, verbose_name=u"Your case name  : ", help_text=u"Make your title attention-grabbing and informative.", null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,verbose_name=u"Subject : ", related_name='cases_subject')
    # Produit
    produit = models.CharField(max_length=100000,verbose_name=u"Product :  ",  null=True)
    image_produit = models.ImageField(upload_to='images/',verbose_name=u"Figure associated with the product ", null=True,blank=True)
    date = models.CharField(max_length=100000,verbose_name=u"Date ",  null=True)
    context = RichTextField(max_length=100000,null=True,verbose_name=u"Context : ", help_text=u"Son histoire, le contexte...")
    context_images = models.ImageField(upload_to='images/', verbose_name=u"Figure associated with the context",  null=True,blank=True)
    description= RichTextField(max_length=100000, null=True, verbose_name=u"Product description : ", )
    description_shema = models.ImageField(upload_to='images/',verbose_name=u"Figure associated with the description",null=True,blank=True)
    diagnostic = RichTextField(max_length=100000, verbose_name=u"Diagnosis of novelty : ", null=True)
    diagnostic_shema= models.ImageField(upload_to='images/',verbose_name=u"Figure associated with the diagnosis of novelty : ", null=True,blank=True)
    # processus = models.FileField(upload_to='images/',verbose_name=u"Name", help_text=u"Please enter your name...", null=True, blank=True)
    processus_name = models.CharField(max_length=255, verbose_name=u"Process-title ",  null=True, blank=True)
    processus = RichTextField(verbose_name=u"Description of the innovation process :",  null=True, blank=True)
    processus_shema = models.ImageField(upload_to='images/',verbose_name=u"Figure associated with the description of the innovation process : ",  null=True,blank=True)
    # fin 
    reference= RichTextField(max_length=100000, null=True,verbose_name=u"References " )
    abstract= RichTextField(max_length=100000, null=True,verbose_name=u"Abstract ")
    auteur = models.CharField(max_length=200,null=True,verbose_name=u"The author(s)" )
    created_date = models.DateTimeField(default=timezone.now,verbose_name=u"The date of creation :")
    update_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(default=timezone.now,verbose_name=u"The date of publication", )
    evaluer =  models.BooleanField(default=False, null=True)
    terms_and_conditions=  models.BooleanField( "I have read and agree to the terms of use and Privacy Policy", default=False)

    def summary_history(self):
        return SummaryHistory.objects.filter(case__pk=self.pk).order_by('-version')

    def save(self, *args, **kwargs):
        super(Cases, self).save(*args, **kwargs)
        # save summary history
        summary_history = self.summary_history()
        if not summary_history or self.update_date != summary_history[0].update_date:
            newSummary = SummaryHistory(case=self, update_date=self.update_date)
            newSummary.save()

    def __str__(self):
        return self.title_case

    def publish(self):
        self.published_date = timezone.now()
        self.save()
 
    def update(self):
        self.update_date = timezone.now()
        self.save()

class SummaryHistory(models.Model):
    version = models.IntegerField(editable=False)
    case = models.ForeignKey('Cases', on_delete=models.CASCADE, )
    update_date=models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        unique_together = ('version', 'case',)

    def save(self, *args, **kwargs):
        # start with version 1 and increment it for each book
        current_version = SummaryHistory.objects.filter(case=self.case).order_by('-version')[:1]
        self.version = current_version[0].version + 1 if current_version else 1
        super(SummaryHistory, self).save(*args, **kwargs)





class Storie(models.Model):
    number = models.IntegerField(editable=False)
    story =  models.ForeignKey('Cases', on_delete=models.CASCADE, )




class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # General Informations
    title_comment = models.CharField(max_length=255, verbose_name=u"Title comment ", help_text=u"Make your title attention-grabbing and informative.", null=True, blank=True)
    produit_comment = models.CharField(max_length=125,verbose_name=u"Produit comment ", help_text=u"help text...", null=True)
    date_comment = models.DateTimeField(auto_now_add=True)
    context_comment = RichTextField(null=True,verbose_name=u"Context comment", help_text=u"Son histoire, le contexte...")
    description_comment= RichTextField(null=True, verbose_name=u"Description comment", help_text=u"help text...")
    diagnostic_comment = RichTextField(verbose_name=u"Diagnostic comment", help_text=u"help text...", null=True)
    processus_comment = RichTextField(verbose_name=u"Processus comment", help_text=u"help text...", null=True, blank=True)
    references_comment= RichTextField(null=True,verbose_name=u" References comment", help_text=u"help text...")
    abstract_comment= RichTextField(null=True,verbose_name=u" Abstract comment", help_text=u"help text...")
    comment_date = models.DateTimeField(default=timezone.now,verbose_name=u"Date d’évaluation", help_text=u"help text...")
    case = models.ForeignKey(Cases, on_delete=models.CASCADE, related_name='comment_case')
    state_comment= models.CharField(max_length=6, choices=State_CHOICES, default='green', null=True, blank=True)
    general_remarks= RichTextField(null=True,verbose_name=u" Abstract comment", help_text=u"help text...")

    
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=70,blank=True)
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)
    school= models.ManyToManyField(School ,  related_name='students_school')

   
    def __str__(self):
        return self.user.username




class TakenQuiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='quizzes', null = True)
    quiz = models.ForeignKey(Cases, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)




class Case_publ(models.Model):

    case_publ= models.ForeignKey(Cases, on_delete=models.CASCADE, related_name='cases_public', null = True)
    publish_date = models.DateTimeField(default=timezone.now,verbose_name=u"The publication date")