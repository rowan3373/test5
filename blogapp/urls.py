
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path("", views.index)

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)