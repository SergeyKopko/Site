from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('theme', 'description', 'image_tag')
    search_fields = ('theme',)
    list_filter = ('theme',)
    prepopulated_fields = {"slug": ("theme",)}
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'posititon', 'image_tag', 'description')
    search_fields = ('full_name',)
    list_filter = ('full_name',)
    prepopulated_fields = {"slug": ("full_name",)}
@admin.register(Progess_institution)
class ProgressInstitutionAdmin(admin.ModelAdmin):
    list_display = ('reward', 'description', 'document_tag', 'image_tag')
    search_fields = ('reward',)
    list_filter = ('reward',)
@admin.register(Paid_Services)
class PaidServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_tag', 'price_service')
    earch_fields = ('name',)
    list_filter = ('name','price_service')
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'passport', 'full_name_parent','passport_parent','class_student', 'information_file', 'question_instuction','email')
    search_fields = ('full_name',)
    list_filter = ('full_name',)
    readonly_fields = ['export']
    def export(self, obj):
        url = reverse('export', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}">Выгрузить данные</a>',
            url,
            '#')

    export.short_description = 'Выгрузка данных об Ученике'