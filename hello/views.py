from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Hello World , This is Django!</h1>")
