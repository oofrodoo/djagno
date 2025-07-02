from django.shortcuts import render
from django.http import HttpResponse
# from post.models import post
# Create your views here.

def post(request):
    return HttpResponse('Hello World')

def list_post (request):
    return render(request, "post/list.html")
