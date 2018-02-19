from django.contrib.auth.models import User
from backend.models import Source
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SourceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = ('title', 'author', 'language', 'color', 'isFile', 'url', 'category', 'file', 'tags')
    #
    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     source = Source.objects.create(**validated_data)
    #
    #     for tag in tags_data:
    #         print(tag)
    #         name = tag.get("name")
    #         t, created = Tag.objects.get_or_create(name=name)
    #         t.save()
    #         source.tags.add(t)
    #     source.save()
    #     return source