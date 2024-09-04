from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<token>[a-z0-9]{10})/$', views.receiver, name='receiver'),
    re_path(r'^logout/?$', views.logout_user, name='logout'),
    re_path(r'^about/?$', views.about, name='about'),
]
