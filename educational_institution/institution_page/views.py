import pprint

from django.shortcuts import render, get_object_or_404, redirect
import shutil
import os
from .forms import CreateApplicationsForm
from .models import *



# Create your views here.

def MainVindowInstitutions(request):
    link_address = 'institution_page/main_window.html'
    title = 'БЭУ | Белорусский Экономический Университет'
    form = Blog.objects.all().order_by('-id')[:4]
    context = {
        'title': title,
        'form': form
    }
    return render(request, link_address, context=context)


def show_Article(request, article_slug):
    article = get_object_or_404(Blog, slug=article_slug)
    link_address = 'institution_page/article.html'
    context = {
        'article': article

    }
    return render(request, link_address, context=context)


def TeachersList(request):
    link_address = 'institution_page/teachers_information.html'
    form = Teacher.objects.all()
    context = {
        'form': form
    }
    return render(request, link_address, context=context)


def show_Teacher(request, teacher_slug):
    teacher = get_object_or_404(Teacher, slug=teacher_slug)
    form = Teacher.objects.values('photo')
    link_address = 'institution_page/teacher.html'
    context = {
        'teacher': teacher,
        'form': form

    }
    return render(request, link_address, context=context)


def CreateApplication(request):
    link_address = 'institution_page/createapplication.html'
    form = CreateApplicationsForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = CreateApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #Cделал после сохранения, чтобы на ПК администратора выгружались данные о пользователе у него ра рабочем столе :)
            name = request.POST.get('full_name')
            file_text = list(request.FILES['information_file'])
            #Создаем папку на рабочем столе
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            folder = os.path.join(desktop, "Документы_о_Студентах")
            if not os.path.exists(folder):
                os.makedirs(folder)
            # Сохраняем файл в папке
            file_path = os.path.join(folder, str(name))
            with open(file_path+'.txt', "w",  encoding="utf-8") as file:
                file.write("\n".join(str(item, encoding="utf-8") for item in file_text))
            return redirect('main_window')
    return render(request, link_address, context=context)

import zipfile
from io import BytesIO
from django.http import HttpResponse
from .models import Student

def export_data(request, pk):
    # получаем данные из базы данных
    data = Student.objects.get(pk=pk)

    # создаем архив с данными формы
    buffer = BytesIO()
    zip_file = zipfile.ZipFile(buffer, 'w')
    zip_file.writestr(f'{data.full_name}.txt', f'ФИО Ученика: {data.full_name}\nПаспорт: {data.passport}\nРодитель: {data.full_name_parent} \nПаспорт родителя: {data.passport_parent}\nКласс: {data.class_student}\nВопрос: {data.question_instuction}\nПочта: {data.email}')
    student_data = data.information_file.read()
    zip_file.writestr('доп_информация_о_ребёнке.txt', student_data)
    zip_file.close()

    # отправляем архив пользователю
    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=form_data.zip'
    return response



def InfoList(request):
    link_address = 'institution_page/info_list.html'

    context = {

    }
    return render(request, link_address, context=context)


def ProgressInstitution(request):
    link_address = 'institution_page/progress_institution.html'
    form = Progess_institution.objects.all()
    context = {
        'form': form
    }

    return render(request, link_address, context=context)



def PaidServices(request):
    link_address = 'institution_page/paid_services.html'
    form = Paid_Services.objects.all().order_by('-id')[:4]
    context = {
        'form': form
    }
    return render(request, link_address, context=context)

def ShowService(request, service_slug):
    service = get_object_or_404(Paid_Services, slug=service_slug)
    link_address = 'institution_page/service.html'
    context = {
        'service': service

    }
    return render(request, link_address, context=context)

def InfoAboutUs(request):
    link_address = 'institution_page/info_about_us.html'
    context = {
    }
    return render(request, link_address, context=context)

def ContactInfo(request):
    link_address = 'institution_page/contact_info.html'
    context = {
    }
    return render(request, link_address, context=context)