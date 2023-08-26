from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Adv(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_auction = models.BooleanField()
    image = models.ImageField()

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=60)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместан ли торг", help_text="Отмеетьте, если торг по объявлению уместен.")
    updated_ad = models.DateTimeField("дата обновления", auto_now=True)
    created_ad = models.DateTimeField("дата публикации", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to="advertisements")


    @admin.display(description="дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_ad.date() == timezone.now().date():
            created_time = self.created_ad.time().strftime("%H:%M")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_ad.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_ad.date() == timezone.now().date():
            updated_time = self.updated_ad.time().strftime("%H:%M")
            return format_html(
                "<span style='color: orange; font-weight: bold'>Сегодня в {}</span>", updated_time
            )
        return self.updated_ad.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="изображение")
    def photo(self):
        if self.image:
            return format_html(
                "<img src= '{}' width = '100px' heigth = '100px' >",
                self.image.url
            )
        return None

    class Meta:
        db_table = "advertisements"
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, is_auction={self.is_auction})"
