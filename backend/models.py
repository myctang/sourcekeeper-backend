from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, default='source')

    def __unicode__(self):
        return self.name

class Source(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default='white')
    isFile = models.BooleanField(default=False)
    link = models.TextField(default='')
    file = models.FileField(upload_to='uploads/', null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('title',)