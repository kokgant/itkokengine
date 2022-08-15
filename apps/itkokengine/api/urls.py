# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from apps.itkokengine.api.views import ClientViewSet

router = DefaultRouter()

router.register(r"clients", ClientViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

