# -*- encoding: utf-8 -*-
"""
Copyright (c) 2020 - Kokgant
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", include("apps.authentication.urls",),),
    path("api/itkokengine/", include("apps.itkokengine.api.urls"), name="itkokengine"),
    path('logs/', include('log_viewer.urls')),
    path('api-auth/', include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
