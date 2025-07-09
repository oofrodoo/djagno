from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from .models import Post
from django.urls import reverse_lazy  # Use reverse_lazy for class-based views


# def list_post_view(request):
#     posts = Post.objects.all()  # Use correct query to fetch all posts
#     return render(
#         request,
#         "post/list.html",
#         context={
#             "all_post": posts
#         }
#     )


# def add_post_view(request):
#     context = {
#         "author": User.objects.all()
#     }
#     return render(request, template_name="post/form.html")


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'body', 'author']  # adjust fields as needed
    template_name = 'post/form.html'
    success_url = reverse_lazy("list-post")  # Use reverse_lazy for CBVs


def list_post(request):
    all_posts = Post.objects.all()
    return render(request, "post/list.html", {"all_posts": all_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = "post/details.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/delete.html"
    success_url = reverse_lazy("list-post")

class ListPostView(ListView):
    template_name = "post/list.html"
    context_object_name = "all_posts"

    def get_queryset(self):
        current_user = self.request.user  
        posts = Post.objects.filter(author=current_user)
        return posts