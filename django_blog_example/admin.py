from django.contrib import admin

from django_blog_example import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Comment)
