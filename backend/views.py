from backend.serializers import SourceSerializers, UserSerializers
from backend.models import Source
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SourceList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tags', 'color', 'author', 'language',)


class SourceDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)