# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - Kokgant
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name = "core"

urlpatterns = [
    path("token/", obtain_auth_token, name="token"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)