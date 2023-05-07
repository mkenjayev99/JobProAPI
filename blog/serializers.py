from rest_framework import serializers
from .models import Blog, Category, Tag, SubImage, SubContent, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class SubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubImage
        fields = ['id', 'image']


class SubContentSerializer(serializers.ModelSerializer):
    images = SubImageSerializer(read_only=True)

    class Meta:
        model = SubContent
        fields = ['id', 'title', 'content', 'images']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'parent_comment', 'created_date', 'top_level_comment_id']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'comments', 'image', 'date_created']


class BlogSingleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcontent = SubContentSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'image', 'subcontent',
                  'category', 'tags', 'comments', 'date_created', 'date_modified']

