from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from posts.models import Post,Tag, Category
from posts.forms import PostForm, CommentForm
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
    post = get_object_or_404(Post, id=pk)#post = Post.objects.get() bul jakta http 500 kaitarat
    post.views += 1
    post.save()
    return render(r, "posts/post_detail.html", {"post": post})

def create_post(request: HttpRequest) -> HttpResponse:#type hinting
    form = PostForm()
    if request.method.lower() == "post":
     print(request.POST)
     form = PostForm(request.POST, request.FILES)
     if form.is_valid():
            form.save()
            return redirect("post_detail", pk=form.instance.pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, "posts/create_post.html", {"form": form, "tags": tags, "categories": categories})

def post_comment(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method.lower() == "post":
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=pk)
    return render(request, "post_detail.html", {"post":post})

def delete_post(request: HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method.lower() == "post":
        post.delete()
        print("Post deleted!")
        return redirect("post_list")
        

    return render(request, "posts/post_delete.html", context={"post": post})
