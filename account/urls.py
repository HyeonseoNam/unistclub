from django.conf.urls import url, include
from account import views
# from account import UserCreateView, UserCreateDoneTV

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', include('django.contrib.auth.urls')),
    # url(r'^register/$', UserCreateView.as_view(), name='register'),
    # url(r'^register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    ## 로그인을 위한 임시 코드
    # url(
    #     r'^accounts/login/',
    #     auth_views.login,
    #     name='login',
    #     kwargs={
    #         'template_name': 'login.html'
    #     }
    # ),
    # url(
    #     r'^accounts/logout/',
    #     auth_views.logout,
    #     name='logout',
    #     kwargs={
    #         'next_page': settings.LOGIN_URL,
    #     }
    # ),
]
