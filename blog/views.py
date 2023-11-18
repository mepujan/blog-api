from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog, Comment
from .serializers import BlogSerializers, CommentSerializers


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class BlogRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers


class CommentsListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
