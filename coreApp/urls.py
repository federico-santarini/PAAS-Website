from django.urls import path

from coreApp.views import index

urlpatterns = [
    path("", index, name="index"),
]
