from django.contrib import admin
from django.urls import path
from post.views import list_post, add_post_view, CreatePostView, PostDetailView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list-post/", list_post, name = "list-post"),
    path("add-post/", add_post_view, name = "add-post"),
    path("create-post/", CreatePostView.as_view(), name = "create-post"),
    path("post-detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post-delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"),
]


#bibek yadav bhaisa ka dud lene gaya.
#yadav ji
#jay shree ram
