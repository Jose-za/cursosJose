# Generated by Django 4.0.5 on 2022-08-03 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_actividad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['-created'], 'verbose_name': 'Descripciones', 'verbose_name_plural': 'Descripción'},
        ),
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='edad',
        ),
    ]
