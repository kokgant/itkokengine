# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import (
    ClientViewSet,
)

app_name = "itkokengine"

router = DefaultRouter()
router.register(r"clients", ClientViewSet, basename="clients")

urlpatterns = [
    path("token/", obtain_auth_token, name="token"),
]
