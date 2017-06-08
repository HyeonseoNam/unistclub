from django.conf.urls import url, include
from account import views
# from account import UserCreateView, UserCreateDoneTV

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout, login
from .views import signup, account_detail, account_change


urlpatterns = [
    # url(r'^$', include('django.contrib.auth.urls')),

    # signup form 화면
    url(r'^signup/$', signup, name='signup'),
    # signup submit 후 완료화면
    url(r'^signup_ok/$', TemplateView.as_view(template_name='registration/signup_ok.html'), name='signup_ok_url'),



    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {
        # logout 시 이동하는 페이지. login_url 경로 변경시 절대값경로로 변경해야한다.
        # 'next_page': '/accounts/login',
        'next_page': '/',
    }, name='logout'),
    url(r'^detail/$', account_detail, name='account_detail'),
    url(r'^change/$', account_change, name='account_change'),



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
