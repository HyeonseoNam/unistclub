from django.shortcuts import render, render_to_response,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login, logout
from .models import UcUser
from group.models import Membership, Group, Comment
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

# email 인증
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# from django.contrib.auth.models import User
from django.core.mail import EmailMessage


#
#
# def login(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # TODO: is_active 필드 구현, false시 로그인 x
#             # if user.is_active:
#                 login(request, user)
#                 # 로그인 시 가장 먼저보일 url
#                 return HttpResponseRedirect('/')
#
#
#     return render_to_response(
#             '/registration/login.html',
#             context_instance=RequestContext(request)
#     )

# login이 필요한 view의 경우 데코레이터 추가
# @login_required(login_url='/accounts/login/')

# custom_login
def custom_login(request, *args, **kwargs):
    # 만약에 유저가 로그인 되어있다면 메인으로 보내기
    if request.user.is_anonymous:
        return login(request, *args, **kwargs)
    elif request.user:
        return redirect('/')
    elif not request.user.is_active:
        return redirect('/')
    else:
        return login(request, *args, **kwargs)

def signup(request):
    """
    signup to register users
    """
    # 만약에 유저가 로그인 되어있다면 메인으로 보내기
    if request.user.is_anonymous:
        pass
    elif request.user:
        return redirect('/')

    template = 'registration/signup.html'
    userForm = UserCreationForm()
    message = ""
    # 가입 양식 작성하하여 제출 시 POST
    if request.method == "POST":
        userForm = UserCreationForm(request.POST, request.FILES or None)
        # valid할 경우만 저장 TODO:is_valid() 양식에 맞게 생성필요.
        if userForm.is_valid():
            # userForm.save()
            user = userForm.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject, message)
            toemail = userForm.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[toemail])
            email.content_subtype = "html"
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

            # return HttpResponseRedirect(
            #     reverse("account:login")    #
            # )
        else:
            message="패스워드가 일치하지 않습니다."

    # 가입 양식 미작성 시 GET. 아무처리하지 X
    elif request.method == "GET":
        pass

    context = {"userForm" : userForm, "message": message}
    return render(request, template, context)

@login_required(login_url='/accounts/login')
def account_detail(request, user_id):
    user = get_object_or_404(UcUser, user_id=user_id)
    joined_group_list = []
    waiting_group_list = []
    mycomments = []
    membership_joined = Membership.objects.filter(member=user, status=True)
    membership_waiting = Membership.objects.filter(member=user, status=False)
    for m in membership_joined:
        joined_group_list.append(m.group)

    for m in membership_waiting:
        waiting_group_list.append(m.group)

    mycomments = Comment.objects.filter(user=user)
    # 멤버십에서 joined, waiting인 멤버십 쿼리셋 뽑기

    template = 'account/account_detail.html'
    context={
        'user': user,
        'joined_groups':joined_group_list,
        'waiting_groups':waiting_group_list,
        'mycomments':mycomments}
    return render(request, template, context)

@login_required(login_url='/accounts/login')
def account_change(request):
    user = request.user
    form = UserChangeForm(instance=user)
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES or None, instance=user)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.save()
            form.save(user)
            return redirect('/accounts/detail/')

    template = 'account/account_change.html'
    context = {
        "form": form,
    }
    return render(request, template, context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UcUser.objects.get(user_id=uid)
    except(TypeError, ValueError, OverflowError, UcUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')