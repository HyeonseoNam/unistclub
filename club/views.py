from django.shortcuts import render

# Create your views here.

def club_each(request):
    template = 'club/each.html'
    context = {}
    return render(request, template, context)