from django.db import models


class Project(models.Model):
    # Заголовок с названием проекта.
    title = models.CharField(max_length=100)
    # Краткое описание проекта.
    description = models.CharField(max_length=250)
    # Изображение главной страницы проекта.
    image = models.ImageField(upload_to='portfolio/images/')
    # Ссылка на проект в Интернете.
    url = models.URLField(blank=True)

