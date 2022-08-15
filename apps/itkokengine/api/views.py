# -*- coding: utf-8 -*-

import json
import calendar
from datetime import datetime
import logging.config

from rest_framework import status
from rest_framework import exceptions, mixins, parsers, status, views, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.http import Http404
from django.conf import settings
from django.apps import apps

from ..models import Client
from .serializers import (
    ClientSerializer
)

logger = logging.getLogger("itkokengine")


class ClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ClientBriefSerializer
    #     else:
    #         return ClientSerializer

    def get_queryset(self):
        clients = Client.objects.all()
        
        return clients
    

    # @action(methods=['POST'], url_path='subscribe-sofia', detail=False)
    # def subscribe_sofia(self, request):
    #     """Llama a synchro a topdigital/subscribe

    #     Args:
    #         Lista de nifs. Anota en synchro un registro para realizar el alta

    #     Returns:
    #         {"res": True or False} 
    #     """
    #     nifs = self.request.query_params.get("nifs", None)
    #     if isinstance(nifs, str) and nifs:  
    #         try:
    #             url = settings.SYNCHRO_SUBSCRIBE_SOFIA_URL
    #             #logger.info(url)
    #             headers = {
    #                 "Authorization": f"Token {settings.APPSESORIA_TOKEN_ACCESS_SYNCHRO}",
    #                 "Content-Type": "application/json",
    #                 "Connection": "close"
    #             }
    #             params = {"nifs":nifs}
    #             url_parse = urlparse.urlparse(url)
    #             query = url_parse.query
    #             url_dict = dict(urlparse.parse_qsl(query))
    #             url_dict.update(params)
    #             #url_new_query=f"nifs={url_dict['nifs']}"
    #             url_new_query = urlparse.urlencode(url_dict)
    #             url_parse = url_parse._replace(query=url_new_query)
    #             new_url = urlparse.urlunparse(url_parse)
    #             response = requests.request("POST", new_url, headers=headers)
    #             status_code=response.status_code
    #         except Exception as e:
    #             logger.exception(f"Error en alta sofia {nifs}\nExcepcion:{e}")
    #             ok = False
    #         else:
    #             if response.status_code in [200,201]:                    
    #                 return Response({"OK": True}, status=status.HTTP_200_OK)
    #             else:
    #                 return Response({"Error": f"Error en alta sofia {response.status_code}"},status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"Error": f"Parámetros incorrectos alta sofia"},status=status.HTTP_400_BAD_REQUEST)            
