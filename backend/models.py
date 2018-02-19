from django.db import models

class Source(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, default='white')
    isFile = models.BooleanField(default=False)
    url = models.TextField(default='')
    file = models.FileField(upload_to='uploads/', null=True)
    tags = models.TextField(default='')
    category = models.CharField(max_length=50, default='article')

    class Meta:
        ordering = ('title',)