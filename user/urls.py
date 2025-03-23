from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Register, LoginUser, Dashboard, UpdateUser, LogoutUser, UpdateUserImage

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('update-user/', UpdateUser.as_view(), name='update-user'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('update-image/', UpdateUserImage.as_view(), name='update-image')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)