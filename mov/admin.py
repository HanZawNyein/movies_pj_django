from django.contrib import admin
from .models import Category,Movie,MovieImage,DriveName,MovieURL,SeriesURL

# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MovieImage)
admin.site.register(DriveName)
admin.site.register(MovieURL)
admin.site.register(SeriesURL)