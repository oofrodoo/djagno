from django.contrib import admin
from django.urls import path
from post.views import  CreatePostView, PostDetailView, PostDeleteView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("create-post/", CreatePostView.as_view(), name = "create-post"),
    path("post-detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post-delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
]



