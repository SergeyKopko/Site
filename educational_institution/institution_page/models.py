from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


#Модель подачи документов ученика
class Student(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='ФИО ученика')
    passport = models.CharField(max_length=50, verbose_name='Паспорт ученика')
    full_name_parent = models.CharField(max_length=50, verbose_name='ФИО родителя')
    passport_parent = models.CharField(max_length=50, verbose_name='Паспорт родителя')
    class_student = models.IntegerField(verbose_name="Номер класса ученика")
    information_file = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name="Файл с информацией об ученике", null = True)
    question_instuction = models.CharField(blank=True, null=True, verbose_name="Вопрос учреждению", max_length=700)
    email = models.EmailField(blank=True, null=True, verbose_name="Почта") #ответ на вопрос будет прилетать туда

    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'


#Модель о блоге(новости и иная информация учреждения)
class Blog(models.Model):
    theme = models.CharField(max_length=100, verbose_name="Название статьи")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name="Описание статьи")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фотография к статье", null=True)

    def __str__(self):
        return self.theme

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.photo.url))

    image_tag.short_description = 'Фотография'

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    class Meta:
        verbose_name = 'Блоги'
        verbose_name_plural = 'Блоги'

#Модель для карточки преподавателя
class Teacher(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='ФИО преподавателя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    posititon = models.CharField(max_length=100, verbose_name="Должность и предмет обучения")
    description = models.TextField(verbose_name="Информация о карьере преподавателя")
    photo = models.ImageField(upload_to='photos_teacher/%Y/%m/%d/', verbose_name="Фотография преподавателя", null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.photo.url))

    image_tag.short_description = 'Фотография'

    def get_absolute_url(self):
        return reverse('information_teacher', kwargs={'teacher_slug': self.slug})

    class Meta:
        verbose_name = 'Преподаватели'
        verbose_name_plural = 'Преподаватели'


#
class Progess_institution(models.Model):
    reward = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to='files_reward/%Y/%m/%d/', verbose_name="Документы наград / лицензий")
    photo = models.ImageField(upload_to='progress_photo/%Y/%m/%d/', verbose_name="Фотография под документ(необязательно)", null=True, blank=True)

    class Meta:
        verbose_name="Достижения/лицензии"
        verbose_name_plural = 'Достижения/лицензии'

    def document_tag(self):
        return mark_safe('<a href="%s">%s</a>' % (self.file.url, self.reward))

    document_tag.short_description = 'Документ'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.photo.url))

    image_tag.short_description = 'Фотография'

class Paid_Services(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название услуги')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание услуги')
    photo = models.ImageField(upload_to='p_servicesPhoto/%Y/%m/%d/', verbose_name="Фотография")
    price_service = models.TextField(verbose_name='Стоимость услуги')

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.photo.url))

    image_tag.short_description = 'Фотография'


    def get_absolute_url(self):
        return reverse('information_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name="Платные услуги"
        verbose_name_plural = 'Платные услуги'