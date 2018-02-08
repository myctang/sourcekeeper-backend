from django.contrib.auth.models import User
from backend.models import Source
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SourceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('title', 'author', 'language')