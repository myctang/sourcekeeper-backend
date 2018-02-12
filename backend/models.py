from django.db import models

class Tag(models.Model):
    Name = models.TextField

class Source(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default='white')
    isFile = models.BooleanField
    link = models.TextField
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('title',)
