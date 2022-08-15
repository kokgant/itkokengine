# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - Kokgant
"""
from typing import Iterable, Optional

import logging
from decouple import config
from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import mail_admins
from django.apps import apps

logger = logging.getLogger("itkokengine")
# logger = logging.getLogger("consola")

class Client(models.Model):

    STATE_ACTIVE = "Activo"
    STATE_INACTIVE = "Baja"
    STATE_BLOQUED = "Bloqueado"
    STATE_CHOICES = [
        (STATE_ACTIVE, _("Activo")),
        (STATE_INACTIVE, _("Baja")),
        (STATE_BLOQUED, _("Bloqueado")),
    ]

    # Datos personales
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    vat = models.CharField(verbose_name=_("VAT"), max_length=15, null=True, blank=True,)
    phone = models.CharField(verbose_name=_("Phone"), max_length=255, blank=True, null=True,)
    mobil = models.CharField(verbose_name=_("Mobil phone"), max_length=255, blank=True, null=True,)
    email = models.EmailField(verbose_name=_("Main email"), max_length=255)
    address = models.CharField(verbose_name=_("Address"), max_length=255, blank=True, null=True,)
    observations = models.TextField(verbose_name=_("Observations"),blank=True, null=True,)
    state_client = models.CharField(verbose_name=_("State"), max_length=50, choices=STATE_CHOICES, default=STATE_ACTIVE, null=True, blank=False)

    created_at = models.DateTimeField(verbose_name=_("Created at"), editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated at"), editable=False, auto_now=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return '{} {} {} (#{})'.format(_('Client'), self.name, self.vat, self.pk)
