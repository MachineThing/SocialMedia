from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
