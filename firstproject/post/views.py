from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post
# Create your views here.

def post(request):
    return HttpResponse('Hello World')

def list_post (request):
    posts = Post.objects.all()
    return render(request, "post/list.html")
    context = {
        "posts":posts
    }

