from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import GroupForm, CommentForm
from .models import Group, Comment, Membership
from account.models import UcUser
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
    template = 'group/group_detail.html'
    comment_form = CommentForm()
    # 지원 가능한 인스턴스만 부를때!
    # group_instance = Group.objects.is_apply()
    group_instance = Group.objects.all()
    group = get_object_or_404(group_instance, id=group_id)

    # 그룹에 지원한 사람, 그룹에 들어간 사람과 그룹간의 관계 데이터
    group_membership = group.membership_set

    # 지원한 사람 관계 데이터
    applied_members = group_membership.filter(status=False)
    applied_list = []

    # 그룹에 들어간 사람 관계 데이터
    joined_members = group_membership.filter(status=True)
    joined_list = []

    # 관계 데이터에서 이름 뽑기(지원한 사람)
    for am in applied_members:
        applied_list.append(am.member)

    # 관계 데이터에서 이름 뽑기(그룹에 들어간 사람)
    for jm in joined_members:
        joined_list.append(jm.member)

    # TODO 좋은 방법 아니므로 좀더 좋은 방법 모색하기

    # comment 불러오기
    comments = Comment.objects.filter(group=group)

    if request.POST:
        # comment 작성
        if request.is_ajax():
            comment_form = CommentForm(request.POST or None, request.FILES or None)
            if comment_form.is_valid():
                passed_content = request.POST['comment_content']
                instance = comment_form.save(commit=False)
                instance.group = group
                instance.content = passed_content
                instance.user = request.user # merge: 로그인 user 등록
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
                data = {'comment_user': instance.user, 'added_comment': instance.content, 'comment_created': ajax_datetime}
                json_data = json.dumps(data, sort_keys=True, default=str)
                return HttpResponse(json_data, content_type='application/json')
            else:
                pass
        # 참가신청하기
        else:
            if Membership.objects.filter(member=request.user, group=group).exists():
                context = {'group': group, 'comment_form': comment_form, 'comments': comments,
                           'message': '이미 신청했습니다.','applied_list': applied_list, 'joined_list':joined_list}
            else:
                membership = Membership(group=group, member=request.user)
                membership.save()
                # 그룹에 지원한 사람, 그룹에 들어간 사람과 그룹간의 관계 데이터
                group_membership = group.membership_set
                # 지원한 사람 관계 데이터
                applied_members = group_membership.filter(status=False)
                applied_list = []
                # 관계 데이터에서 이름 뽑기(지원한 사람)
                for am in applied_members:
                    applied_list.append(am.member)

                context = {'group': group, 'comment_form': comment_form, 'comments': comments,
                           'message': '신청이 완료되었습니다.','applied_list': applied_list, 'joined_list':joined_list}

            return render(request, template, context)

    context = {'group': group, 'comment_form': comment_form, 'comments': comments,
               'applied_list': applied_list, 'joined_list':joined_list}
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
            instance.admin = request.user # merge: 로그인 user 등록
            instance.save()
            return redirect('group_main')
        else:
            pass

    return render(request, template, context)