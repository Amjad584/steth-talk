from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def newsfeed(request):
    posts = Posts.objects.all().order_by("date")
    return render(request,"posts/newsfeed.html", {'posts':posts})

def post_detail(request,slug):
    #return HttpResponse(slug)
    post = Posts.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html',{'post': post})

@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            value = form.save(commit=False)
            value.author = request.user
            value.save()
            return redirect('posts:newsfeed')
    else:   
        form = forms.CreatePost()
    return render(request,'posts/post_create.html', {'form':form})