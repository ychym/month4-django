"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from posts.views import (
        HelloWorldView, 
        MyName,
        PostListView,
        PostDetailView,
        CreatePostView, 
        PostCommentView, 
        DeletePostView, 
        EditPostView, 
        MyPostsView,
    )
from django.conf import settings
from user.views import register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", HelloWorldView.as_view()),
    path("name/", MyName.as_view()),
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", CreatePostView.as_view(), name="create_post"),
    path("post/<int:pk>/comment/", PostCommentView.as_view, name="post_comment"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_post"),
    path("post/<int:pk>/edit/", EditPostView.as_view(), name="edit_post"),
    path("accounts/register", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("post/myposts", MyPostsView.as_view(), name="my_posts"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)