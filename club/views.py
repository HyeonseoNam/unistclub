from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Club
from .forms import ClubForm

# Create your views here.

def club_main(request):
    template = 'club/club_main.html'
    # if request.method == 'POST':
    #     search_content = request.POST['search_content']
    #     groups = Group.objects.filter(group_name__contains=search_content)
    # else:
    clubs = Club.objects.all()

    context = {'clubs': clubs}
    return render(request, template, context)

def club_detail(request, club_id):
    template = 'club/club_detail.html'
    context = {}
    return render(request, template, context)

def club_create(request):
    form = ClubForm()
    template = 'club/club_create.html'
    context = {"form": form}

    # 저장하기 눌렀을 경우
    if request.method == 'POST':
        form = ClubForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            # 나중에 로그인했을때 로그인 유저가 바로 들어가게
            # instance.admin_id = request.user.id
            # instance.admin_id = 1
            instance.save()
            return redirect('club_main')
        else:
            pass

    return render(request, template, context)