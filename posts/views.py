from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from posts.models import Post
# Create your views here.

def hello_world(r):
    return HttpResponse("<h1>Hello world!</h1>")

def my_name(r):
    name = "Yrysgul"

    return HttpResponse(f"<h2>Hello,</h2><h1>{name}</h1>")

def say_name(r, name):
    return HttpResponse(f"<h2>Hello,</h2><h1>{name}</h1>")

def post_list(r):#r-request
    posts = Post.objects.filter(is_published=True)

    return render(r, "posts/list_posts.html", {"posts":posts})

def post_detail(r, pk):
    post = get_object_or_404(Post, id=pk)
    #post = Post.objects.get()
    return render(r, "posts/post_detail.html", {"post": post})

