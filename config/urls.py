from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('user/', include('app_authentication.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
