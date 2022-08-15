# -*- coding: utf-8 -*-

from apps.itkokengine.models import Client

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

class ClientSerializer(serializers.ModelSerializer):
    
    clusters_data = serializers.SerializerMethodField()
    subscription_plan = serializers.SerializerMethodField()
    chat = serializers.SerializerMethodField()
    year_seats = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = "__all__"
        extra_fields = ['clusters_data','year_seats']

    def get_year_seats(self, obj):
        return {c.year:c.seats for c in ClientSeatsYear.objects.filter(client__id=obj.id)}
        
    def get_clusters_data(self, obj):
        
        cluster_data=obj.get_cluster()
        if cluster_data:
            try:
                cluster_data={
                    "id": cluster_data.id,
                    "name":cluster_data.name,
                }
            except:
                cluster_data={
                    "id": "",
                    "name":"No localizado",
                }
        return cluster_data
    
    def get_subscription_plan(self, obj):
        sub_active = obj.get_subscription_active()
        return sub_active.plan if sub_active else "Ninguna"
        
    def get_ia_date_active_subscription_alta(self, obj):
        sub_last = obj.subscription_set.order_by('-date_start').first()
        return sub_last.date_start if sub_last else None
        
    def get_ia_date_active_subscription_baja(self, obj):
        sub_last = obj.subscription_set.order_by('-date_start').first()
        return sub_last.date_end if sub_last else None

    def get_chat(self, obj):
        serializer = ChatSerializer(instance=obj.get_chat())
        return serializer.data
    
    def update(self, instance, validated_data):
        #cli = Client.objects.get(pk=instance.id)
        #cli.update(**validated_data)
        #instance.state_client = validated_data.get("state_client",instance.state_client)
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()        
        return instance
    