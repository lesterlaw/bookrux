from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='booklist'),
    url(r'^info/(?P<slug>[\w.@+-]+)/$', views.BookDetail.as_view(), name='bookdetail'),
    url(r'^sell/', views.AddBook, name='addbook'),
    url(r'^edit/(?P<slug>[\w.@+-]+)/$', views.EditBook, name='editbook'),
    url(r'^delete/(?P<slug>[\w.@+-]+)/$', views.DeleteBook, name='deletebook'),
    url(r'^genre/$', views.GenreList.as_view(), name='genrelist'),
    url(r'^genre/(?P<genre>[\w.@+-]+)/$', views.GenreDetail, name='genredetail'),
    url(r'^charge/(?P<slug>[\w.@+-]+)/$', views.charge, name='charge'),
    url(r'^sold/(?P<slug>[\w.@+-]+)/$', views.sold, name='sold'),
]