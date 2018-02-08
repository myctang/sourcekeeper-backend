from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from backend.serializers import UserSerializers, SourceSerializers
from backend.models import Source
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class SourceList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SourceDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)