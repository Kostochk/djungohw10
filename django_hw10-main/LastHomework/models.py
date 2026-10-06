from django.db import models
from django.contrib.auth.models import User

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader_profile', null=True, blank=True)
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone = models.CharField(max_length=15, verbose_name="Контактний телефон")
    email = models.EmailField(verbose_name="Email")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата запису")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    publication_year = models.IntegerField(verbose_name="Рік видання")
    style = models.CharField(max_length=100, verbose_name="Стиль/Жанр")
    publisher = models.CharField(max_length=100, verbose_name="Видавництво")
    
    holder = models.ForeignKey(
        Reader, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='borrowed_books',
        verbose_name="У кого на руках"
    )

    @property
    def is_available(self):
        """Перевірка наявності книги в бібліотеці"""
        return self.holder is None

    def __str__(self):
        return f"{self.title} — {self.author}"