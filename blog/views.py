from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# data from database

fake_posts = [
  {
    'Author': 'John',
    'title': 'Post No:1',
    'content': 'we are here to learn django framework',
    'date': '27 August 2015',
  },
  {
    'Author': 'Smith',
    'title': 'Post No:2',
    'content': 'we are here to learn django framework with React front-end',
    'date': '27 September 2015',
  }
]


def home(request):
  context = {
    # 'posts' : fake_posts
    'posts' : Post.objects.all(),
  }
  return render(request, 'blog/home.html',context)   

def about(request):
  return render(request, 'blog/about.html')


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 4

class UserPostListView(ListView):
  model = Post
  template_name = 'blog/user_posts.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 4

  def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
  model = Post


class PostCreateView(  LoginRequiredMixin , CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(  LoginRequiredMixin, UserPassesTestMixin , UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  #to check if the author of the post is accessing the post or not.
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False



class PostDeleteView( LoginRequiredMixin , UserPassesTestMixin,DeleteView):
  model = Post
  success_url = '/'
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
  
