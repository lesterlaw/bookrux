from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NoteList.as_view(), name='notelist'),
    url(r'^info/(?P<slug>[\w.@+-]+)/$', views.NoteDetail.as_view(), name='notedetail'),
    url(r'^add/', views.AddNote, name='addnote'),
    url(r'^edit/(?P<slug>[\w.@+-]+)/$', views.EditNote, name='editnote'),
    url(r'^sold/(?P<slug>[\w.@+-]+)/$', views.sold, name='sold'),
    url(r'^delete/(?P<slug>[\w.@+-]+)/$', views.DeleteNote, name='deletenote'),
]