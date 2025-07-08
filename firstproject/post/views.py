from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Post
from post.forms import PostForm




def list_post_view(request):
    posts = Post.objects.all()  # Use correct query to fetch all posts
    return render(
        request,
        "post/list.html",
        context={
            "all_post": posts
        }
    )
def add_post_view(request):
    context = {
        "author": User.objects.all()
    }
    return render (request, template_name= "post/form.html")

class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'body', 'author']  # adjust fields as needed
    template_name = 'post/form.html'
    success_url = '/list-post/'  # or wherever you want to redirect after creation

def list_post(request):
    return render(request, "post/list.html")
