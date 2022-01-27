# Generated by Django 4.0.1 on 2022-01-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_student_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='users.Student'),
        ),
    ]