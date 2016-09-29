from django.shortcuts import render
from django.utils import timezone
from .models import Postear

def post_list(request):
    posts = Postear.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts})