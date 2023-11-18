from django.urls import path
from .views import BlogListCreateAPIView, BlogRetriveUpdateDeleteAPIView, CommentsListCreateAPIView


urlpatterns = [
    path('blogs', BlogListCreateAPIView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogRetriveUpdateDeleteAPIView.as_view(), name='blog'),
    path('comments', CommentsListCreateAPIView.as_view(), name='comments'),
]
