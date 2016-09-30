from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear

def post_list(request):
    posts = Postear.objects.all()
    return render(request, 'blog/lista.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})