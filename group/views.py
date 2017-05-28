from django.shortcuts import render, redirect, get_object_or_404
from .forms import GroupForm
from .models import Group

# Create your views here.
def group_main(request):
    print('group_main')
    groups = Group.objects.all()
    template = 'group/group_main.html'
    context = {'groups': groups}
    return render(request, template, context)

def group_detail(request, group_id):
    print('group_detail')
    # 지원 가능한 인스턴스만 부를때!
    # group_instance = Group.objects.is_apply()
    group_instance = Group.objects.all()
    group = get_object_or_404(group_instance, id=group_id)
    template = 'group/group_detail.html'
    context = {'group': group}
    return render(request, template, context)

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