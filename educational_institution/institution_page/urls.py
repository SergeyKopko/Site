from django.urls import path, include

from .views import *




urlpatterns = [
    path('', MainVindowInstitutions, name='main_window'),
    path('article/<slug:article_slug>/', show_Article, name='article'),
    path('teacher_information', TeachersList, name='teachers_list'),
    path('information_teacher/<slug:teacher_slug>/', show_Teacher, name='information_teacher'),
    path('create_application', CreateApplication, name='application'),
    path('info_list', InfoList, name='info_list'),
    path('progress_institution', ProgressInstitution, name = 'progress_institution'),
    path('paid_services', PaidServices, name = 'paid_services'),
    path('information_service/<slug:service_slug>/', ShowService, name='information_service'),
    path('info_about_us', InfoAboutUs, name="info_about_us"),
    path('contact_info', ContactInfo, name="contact_info"),
    path('export/<int:pk>/', export_data, name='export'),
]

