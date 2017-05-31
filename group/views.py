from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import GroupForm, CommentForm
from .models import Group, Comment
from datetime import datetime
from pytz import timezone
import json
from django.core import serializers

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
    print(request)
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

            se_tz = timezone('Asia/Seoul') # 서울 타임존
            real_datetime = se_tz.normalize(instance.created_at.astimezone(se_tz)) # 서울로 일시 바꾸기
            am_pm = real_datetime.strftime('%p')
            if am_pm=="AM":
                am_pm = "오전"
            else:
                am_pm = "오후"
            ajax_datetime = real_datetime.strftime('%Y년 %m월 %d일 %H:%M ') # 년 월 일 시간까지 입력
            ajax_datetime = ajax_datetime + am_pm # 오전 오후 붙이는 곳
            data = {'comment_user': '1', 'added_comment': instance.content, 'comment_created': ajax_datetime}
            json_data = json.dumps(data, sort_keys=True, default=str)
            return HttpResponse(json_data, content_type='application/json')
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