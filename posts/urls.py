from django.conf.urls import url

from . import views

urlpattern = [
    url(r'^ler.post/(?P<slug>[\w-]+)/$', views.ler_post, name= 'ler-post'),    
]
