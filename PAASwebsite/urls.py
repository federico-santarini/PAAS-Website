"""
URL configuration for PAASwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from coreApp.views import index, collabora, community, glifi, licenza, progetto,download_selected_images, download_all_images

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='home'),
    path('collabora', collabora, name='collabora'),
    path('community', community, name='community'),
    path('glifi', glifi, name='glifi'),
    path('licenza', licenza, name='licenza'),
    path('progetto', progetto, name='progetto'),
    path('index', index, name='index'),
    path('download-selected/', download_selected_images, name='download_selected_images'),
    path('download-all/', download_all_images, name='download_all_images')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
