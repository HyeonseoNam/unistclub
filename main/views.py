from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.user.is_active)
    return render(request, 'main/index.html',)
