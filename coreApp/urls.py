from django.urls import path
from django.utils.translation import gettext_lazy as _

from coreApp.views import index, collabora, community, glifi, licenza, progetto, download_selected_images, download_all_images

urlpatterns = [
    path('collabora', collabora, name=_('collabora')),
    path('', index, name='home'),
    path('community', community, name='community'),
    path('glifi', glifi, name='glifi'),
    path('licenza', licenza, name='licenza'),
    path('progetto', progetto, name='progetto'),
    path('download-selected/', download_selected_images, name='download_selected_images'),
    path('download-all/', download_all_images, name='download_all_images')
]
