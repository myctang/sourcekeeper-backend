from backend.serializers import SourceSerializers
from backend.models import Source
from django.contrib.auth import authenticate, login
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SourceList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Source.objects.all()
    serializer_class = SourceSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('color', 'author', 'language',)


    def get_queryset(self):
        print()
        queryset = Source.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            print(Source.objects.annotate(search=SearchVector('title', 'author', 'language', 'color', 'tags__name')).filter(search=search))
            vector = SearchVector('title', 'author', 'language', 'color', 'tags__name')
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                return Response("Success", status=status.HTTP_202_ACCEPTED)
        return Response("Unsuccess", status=status.HTTP_406_NOT_ACCEPTABLE)