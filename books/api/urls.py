from django.conf.urls import url
from django.contrib import admin

from .views import (
	BookListAPIView,
	BookDetailAPIView,
	BookDeleteAPIView,
	BookUpdateAPIView,
	)

urlpatterns = [
	url(r'^$', BookListAPIView.as_view(), name="list"),
    url(r'^info/(?P<slug>[\w.@+-]+)/$', BookDetailAPIView.as_view(), name='bookdetail'),
    # url(r'^sell/', views.AddBook, name='addbook'),
    url(r'^edit/(?P<slug>[\w.@+-]+)/$', BookUpdateAPIView.as_view(), name='editbook'),
    url(r'^delete/(?P<slug>[\w.@+-]+)/$', BookDeleteAPIView.as_view(), name='deletebook'),
    # url(r'^genre/$', views.GenreList.as_view(), name='genrelist'),
    # url(r'^genre/(?P<genre>[\w.@+-]+)/$', views.GenreDetail, name='genredetail'),
    # url(r'^charge/(?P<slug>[\w.@+-]+)/$', views.charge, name='charge'),
    # url(r'^sold/(?P<slug>[\w.@+-]+)/$', views.sold, name='sold'),
    # url(r'^rent/$', views.rentcomingsoon, name='rentcomingsoon'),
    # url(r'^like/$', views.LikeBook, name='likebook'),
]