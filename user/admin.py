from django.contrib import admin
from .models import Comment, UserImage

@admin.register(Comment)
class UserCommet(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'post')


admin.site.register(UserImage)