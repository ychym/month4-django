from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.http.request import HttpRequest
from django.views.generic import (
    ListView, 
    View, 
    DetailView, 
    CreateView, 
    DeleteView, 
    UpdateView, 
    GenericViewError,

)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from posts.models import Post,Tag, Category, Comment
from posts.forms import PostForm, CommentForm
from django.db.models import Q
# Create your views here.

class HelloWorldView(View):
    def get(self, r):
        return HttpResponse("<h1>Hello world!</h1>")


class MyName(View):
    
    def get(self, r):
        name = "Yrysgul"
        return HttpResponse(f"<h2>Hello,</h2><h1>{name}</h1>")


class PostListView(ListView):
    model = Post
    template_name = "posts/list_posts.html"
    context_object_name = "posts"

    
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_object(self, queryset = None):
        object = super().get_object(queryset)
        object.views += 1
        object.save()
        return object

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["categories"] = Category.objects.all()

        return context

    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user

        return form    

class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("post_list")

    def get_object(self, queryset = None):
        object =  super().get_object(queryset)
        if object.user != self.request.user:
            raise GenericViewError()
        return object

class EditPostView(UpdateView):
    model = Post
    template_name = "posts/edit_post.html"
    form_class = PostForm    

    def get_object(self, queryset = None):
        object = super().get_object(queryset)

        if object.user != self.request.user:
            raise GenericViewError()
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["categories"] = Category.objects.all()
        return context

class PostCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "post_detail.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]  # Базадан Post издөөнүн кереги жок, түз эле ID беребиз!
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.kwargs["pk"]})
      
class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/my_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user)
         