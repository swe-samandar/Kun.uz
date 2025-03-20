from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, contact, detail, error_page, category

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>', detail, name='detail'),
    path('404/', error_page, name='error-page'),
    path('category/<int:pk>', category, name='category'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)