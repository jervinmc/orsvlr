from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from book.views import GetCode,ConfirmedStatus


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/rooms/', include('rooms.urls')),
    path('api/v1/pools/', include('pools.urls')),
    path('api/v1/events/', include('events.urls')),
    path('api/v1/gallery/', include('gallery.urls')),
    path('api/v1/book/', include('book.urls')),
     path('api/v1/code/code/', GetCode.as_view(), name='get_user'),
     path('api/v1/confirmed/status/', ConfirmedStatus.as_view(), name='get_user'),
]