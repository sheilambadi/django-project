from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #display in browser
    #return HttpResponse('Hello Django!!!')

    #render from template
    return render(request, 'posts/index.html', {
        'title' : 'Latest Posts'
    })
