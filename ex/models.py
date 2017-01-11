from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ImportantNote (models.Model):
    title = RichTextUploadingField(blank=True, verbose_name='Важное сообщение на главной странице')

    class Meta:
        verbose_name_plural = 'Важное сообщение на главной странице'


class About (models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок')
    text = RichTextUploadingField(verbose_name='Текст')
    img = models.ImageField(upload_to='images', blank=True, verbose_name='Изборажение (не обязательно)')

    class Meta:
        verbose_name_plural = 'Обо мне/главная страница'

    def __str__(self):
        return self.title


class Excursion (models.Model):
    name = models.CharField(max_length=50, verbose_name='Название экскурсии')
    description = RichTextUploadingField(verbose_name='Описание')
    img = models.ImageField(upload_to='images', blank=True, verbose_name='Изборажение (не обязательно)')
    slug = models.SlugField(unique=True, verbose_name='Адрес')

    class Meta:
        verbose_name_plural = 'Список экскурсий'

    def __str__(self):
        return self.name


class PeopleReg(models.Model):
    event = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='Экскурсия')
    name = models.CharField(max_length=25, verbose_name='Имя')
    email = models.EmailField(verbose_name='почта')
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    date = models.DateTimeField(verbose_name='Дата и время')

    class Meta:
        verbose_name_plural = 'Зарегистрировавшиеся'


class Contacts(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок')
    text = RichTextUploadingField(verbose_name='Текст')
    img = models.ImageField(upload_to='images', blank=True, verbose_name='Изборажение (не обязательно)')

    class Meta:
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Имя'),
    excursion = models.CharField(max_length=50, verbose_name='Экскурсия')
    event_date = models.DateField(verbose_name='Дата посещения')
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Отзыв')


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = RichTextUploadingField(verbose_name='Содержание')
    likes = models.IntegerField(default=0, editable=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title



