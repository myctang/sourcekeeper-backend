from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'items/?$', views.SourceList.as_view(), name='source_list'),
    url(r'items/(?P<pk>[0-9]+)', views.SourceDetail.as_view(), name='source_list'),
]
