from django.shortcuts import render
from .models import Posts

# Create your views here.


def index(request):
    # return HttpResponse('Hello from posts!')
    # get the first ten posts
    posts = Posts.objects.all()[:10]
    context = ***REMOVED***
        'title': 'Latest Posts',
        'posts': posts
    ***REMOVED***
    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)
    context = ***REMOVED***
        'post': post
    ***REMOVED***
    return render(request, 'posts/details.html', context)