from django.shortcuts import render
from .forms import GroupForm

# Create your views here.
def group_create(request):
    form = GroupForm()
    template = 'group/group_create.html'
    context = {"form": form}
    return render(request, template, context)