from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView

urlpatterns = [
  path("",PostListView.as_view(),name="blog_home"),
  path("post/<int:pk>/",PostDetailView.as_view(),name="Post_details"),
  path("post/new/",PostListView.as_view(),name="post-created"),
  path("about/",views.about,name="blog_about"),
]
