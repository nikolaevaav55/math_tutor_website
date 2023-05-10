from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)