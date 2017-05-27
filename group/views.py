from django.shortcuts import render, redirect
from .forms import GroupForm

# Create your views here.
def group_create(request):
    form = GroupForm()
    template = 'group/group_create.html'
    context = {"form": form}

    # 저장하기 눌렀을 경우
    if request.method == 'POST':
        form = GroupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            # 나중에 로그인했을때 로그인 유저가 바로 들어가게
            # instance.admin_id = request.user.id
            instance.admin_id = 1
            instance.save()
            # 메인페이지로 보내기
            # return redirect('main')
            return redirect('group_create')
        else:
            pass

    return render(request, template, context)