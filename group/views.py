from django.shortcuts import render
from .forms import GroupForm

# Create your views here.
def group_create(request):
    form = GroupForm()