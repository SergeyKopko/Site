
from django.forms import ModelForm, TextInput, FileInput, EmailInput
from .models import Student


class CreateApplicationsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'passport', 'full_name_parent', 'passport_parent', 'class_student', 'information_file', 'question_instuction', 'email',]

    widgets = {
        'full_name': TextInput(attrs={
            'placeholder':'Введите ФИО ребёнка'
        }),
        'passport': TextInput(attrs={
            'placeholder':'Введите паспортные данные ребёнка'
        }),
        'full_name_parent': TextInput(attrs={
            'placeholder': 'Введите ФИО одного из родителей'
        }),
        'passport_parent': TextInput(attrs={
            'placeholder': 'Введите паспортные данные родителя'
        }),
        'class_student': TextInput(attrs={
            'placeholder': 'Введите номер класса в который переходит студент'
        }),
        'information_file': FileInput(attrs={
            'placeholder':'Можете прикрепить файл с доп.информацией'
        }),
        'question_instuction': TextInput(attrs={
            'class':'question_instuction',
            'placeholder': 'Задавайте нам вопросы :)'
        }),
        'email': EmailInput(attrs={
            'placeholder': 'Введите вашу почту(туда придёт ответ на ваше сообщение)'
        }),
    }


