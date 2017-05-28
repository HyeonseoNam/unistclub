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
from django.conf.urls import url, include
from django.contrib import admin
from club.views import club_each
from group.views import group_create, group_main, group_detail

urlpatterns = [
    url(r'', include('main.urls', namespace='main')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('account.urls', namespace='account')),
    url(r'^club_each/', club_each, name='club_each'),
    url(r'^group_create/', group_create, name='group_create'),
    url(r'^groups/', group_main, name="group_main"),
    # url(r'^group/', group_main, name='group'),
    url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
    # url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
]
