from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import GroupForm, CommentForm
from .models import Group, Comment
import json

# Create your views here.
def group_main(request):
    template = 'group/group_main.html'
    if request.method == 'POST':
        search_content = request.POST['search_content']
        groups = Group.objects.filter(group_name__contains=search_content)
    else:
        groups = Group.objects.all()

    context = {'groups': groups}
    return render(request, template, context)

def group_detail(request, group_id):
    template = 'group/group_detail.html'
    comment_form = CommentForm()
    # 지원 가능한 인스턴스만 부를때!
    # group_instance = Group.objects.is_apply()
    group_instance = Group.objects.all()
    group = get_object_or_404(group_instance, id=group_id)

    # comment 불러오기
    comments = Comment.objects.filter(group=group)

    # comment 작성
    if request.is_ajax():
        print(request.POST)
        comment_form = CommentForm(request.POST or None, request.FILES or None)
        if comment_form.is_valid():
            passed_content = request.POST['comment_content']
            instance = comment_form.save(commit=False)
            instance.group = group
            instance.content = passed_content
            # 나중에 로그인했을때 로그인 유저가 바로 들어가게
            # instance.user = request.user.id
            instance.user = 1
            instance.save()
            data = {'added_comment': instance}
            return HttpResponse(data)
        else:
            pass

    context = {'group': group, 'comment_form': comment_form, 'comments': comments}
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
            return redirect('group_main')
        else:
            pass

    return render(request, template, context)