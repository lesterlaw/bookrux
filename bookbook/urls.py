"""bookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
import books.views
from books import views
from django.core.urlresolvers import reverse

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Book', views.BookViewSet)
router.register(r'User', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(/)?$', RedirectView.as_view(url='/books/')),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/(?P<slug>[\w.@+-]+)/$',
        books.views.UserProfileDetail.as_view(),
        name='user_profile_detail'),  

    # url(r'^(?P<username>[\w.@+-]+)/$',
    #     books.views.UserProfileDetail,
    #     name='user_profile_detail'),    
    # url(r'^(?P<pk>[0-9]+)/$',
    #     books.views.UserProfileDetail,
    #     name='user_profile_detail'),
    # url(r'^(?P<username>[\w.@+-]+)/update/$',
    #     books.views.UserProfileUpdate,
    #     name='user_profile_edit'),
    url(r'^accounts/(?P<slug>[\w.@+-]+)/update/$',
        books.views.UserProfileUpdate.as_view(success_url="/books/"),
        name='user_profile_edit'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^messages/', include('postman.urls', namespace='postman')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
