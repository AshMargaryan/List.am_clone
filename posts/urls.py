from django.urls import path

from .views import PostListView, PostDetailView, CreatePostView


urlpatterns = [
    path('', PostListView.as_view(),),
    path("<int:pk>", PostDetailView.as_view(),),
    path("create_post", CreatePostView.as_view(),),
]