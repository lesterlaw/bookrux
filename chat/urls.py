from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Redirect, name='redirect'),
    url(r'^inbox/', views.Inbox, name='inbox'),
    url(r'^chat/(?P<slug>[\w.@+-]+)/', views.ChatDetail, name='chatdetail'),
    url(r'^send/(?P<slug>[\w.@+-]+)/', views.SendMessage, name='sendmessage'),
    url(r'^new/(?P<slug>[\w.@+-]+)/', views.CreateChat, name='createchat'),
]