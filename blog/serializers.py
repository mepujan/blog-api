from rest_framework.serializers import ModelSerializer
from .models import Blog, Comment


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializers(ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('title', 'content', 'author', 'comments')
