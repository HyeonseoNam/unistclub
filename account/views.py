from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UserCreationForm
from django.contrib.auth.views import login, logout


def signup(request):
    """
    signup to register users
    """
    template = 'registration/signup.html'
    context = {}
    userform = UserCreationForm()
    # 가입 양식 작성하하여 제출 시 POST
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        # valid할 경우만 저장 TODO:is_valid() 양식에 맞게 생성필요.
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                reverse("account:signup_ok_url")    # signup_ok라는 url으로
            )

    # 가입 양식 미작성 시 GET. 아무처리하지 X
    elif request.method == "GET":
        pass

    context = {"userform" : userform}
    return render(request, template, context)




