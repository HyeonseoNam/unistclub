"""unistclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from club.views import club_detail, club_main, club_create
from group.views import group_create, group_main, group_detail,\
    membership_cancel, membership_participate, group_change, group_delete


urlpatterns = [
    url(r'', include('main.urls', namespace='main')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('account.urls', namespace='account')),
    url(r'^club_create/', club_create, name='club_create'),
    url(r'^clubs/', club_main, name='club_main'),
    url(r'^club/(?P<club_id>\d+)/$', club_detail, name='club_detail'),
    url(r'^group_create/', group_create, name='group_create'),
    url(r'^groups/', group_main, name="group_main"),
    url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
    url(r'^group/membership_cancel', membership_cancel, name="membership_cancel"),
    url(r'^group/membership_participate', membership_participate, name="membership_participate"),
    url(r'^group/change/(?P<group_id>\d+)/$', group_change, name='group_change'),
    url(r'^group/delete/(?P<group_id>\d+)/$', group_delete, name='group_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)