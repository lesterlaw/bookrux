from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ReviewList.as_view(), name='reviewlist'),
    url(r'^info/(?P<slug>[\w.@+-]+)/$', views.ReviewDetail.as_view(), name='reviewdetail'),
    url(r'^add/', views.AddReview, name='addreview'),
    url(r'^edit/(?P<slug>[\w.@+-]+)/$', views.EditReview, name='editreview'),
    url(r'^delete/(?P<slug>[\w.@+-]+)/$', views.DeleteReview, name='deletereview'),
]