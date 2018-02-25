from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector)
from django.shortcuts import Http404, redirect, render, render_to_response
from django.template import TemplateDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Source
from backend.serializers import SourceSerializers


class SourceList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('color', 'author', 'language', 'category', )


    def get_queryset(self):
        queryset = Source.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            print(Source.objects.annotate(search=SearchVector('title', 'author', 'language', 'color', 'tags')).filter(search=search))
            vector = SearchVector('title', 'author', 'language', 'color', 'tags')
            query = SearchQuery(search)
            queryset = Source.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
            return queryset
        
        return queryset


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

class Login(APIView):
    def post(self, request, format=None):
        print(request.body)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                print("Login success")
                login(request, user)
                return Response("Success", status=status.HTTP_202_ACCEPTED)
        return Response("Unsuccess", status=status.HTTP_406_NOT_ACCEPTABLE)

class Logout(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response("Success", status=status.HTTP_202_ACCEPTED)

def index(request):
    print("asd")
    return render_to_response('backend/static/index.html')

def render_template(request, path):
    if path and settings.APPEND_SLASH and not path.endswith('/'):
        return redirect(request.path + '/')

    templates = [
        '%s.html' % path.rstrip('/'),
        '%sindex.html' % path
    ]

    try:
        print(templates)
        return render(request, templates, {'request': request})
    except TemplateDoesNotExist:
        raise Http404('%s can not be found' % request.path)
