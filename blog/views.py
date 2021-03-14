from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView,DetailView,CreateView
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

class PostDetailView(DetailView):
  model = Post


class PostCreateView(  LoginRequiredMixin , CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

