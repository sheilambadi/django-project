from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.

def index(request):
    #display in browser
    #return HttpResponse('Hello Django!!!')

    #display posts in view
    posts = Posts.objects.all()[:10]

    context = {
        'title' : 'Latest Posts',
        'posts' : posts
    }
    #render from template
    return render(request, 'posts/index.html', context)
