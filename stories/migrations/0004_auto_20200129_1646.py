# Generated by Django 2.2.7 on 2020-01-29 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_storie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='abstract',
            field=djrichtextfield.models.RichTextField(max_length=100000, null=True, verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='auteur',
            field=models.CharField(max_length=200, null=True, verbose_name="L(es)'auteur(s)"),
        ),
        migrations.AlterField(
            model_name='cases',
            name='context_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Figure associée au contexte'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de création'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description',
            field=djrichtextfield.models.RichTextField(max_length=100000, null=True, verbose_name='Description du produit'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description_shema',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Figure associée à la description'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='diagnostic_shema',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Figure associée à la diagnostic de la nouveauté'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='image_produit',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Figure associée au produit'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='processus_shema',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Figure associée à la description du processus d’innovation'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='produit',
            field=models.CharField(max_length=100000, null=True, verbose_name='Le produit '),
        ),
        migrations.AlterField(
            model_name='cases',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de publication'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='reference',
            field=djrichtextfield.models.RichTextField(max_length=100000, null=True, verbose_name='Références'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='school_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='stories.School', verbose_name='Sélectionnez votre Etablissement'),
        ),
    ]
