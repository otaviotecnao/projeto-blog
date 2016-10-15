from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sobre-nos/$', views.sobre_nos, name='sobre-nos'),
]
