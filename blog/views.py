from django.http import HttpResponse
from django.shortcuts import render


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
    'posts' : fake_posts
  }
  return render(request, 'blog/home.html',context)   

def about(request):
  return render(request, 'blog/about.html')