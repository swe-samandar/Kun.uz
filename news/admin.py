from django.contrib import admin
from .models import News, Category, Message

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Message)