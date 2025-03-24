from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    index,
    contact,
    detail,
    error_page,
    category,
    like_comment,
    edit_comment,
    delete_comment,
    )

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>', detail, name='detail'),
    path('404/', error_page, name='error-page'),
    path('category/<int:pk>', category, name='category'),
    path('comment/like/<int:pk>/', like_comment, name='like_comment'),
    path('comment/edit/<int:pk>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)