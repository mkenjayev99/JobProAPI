from rest_framework import permissions
from account.permissions import IsAdminUserOrReadOnly
from rest_framework import generics
from .models import Category, Tag, SubContent, Comment, Blog
from .serializers import (
    CategoryBlogSerializer,
    TagBlogSerializer,
    CommentSerializer,
    SubContentSerializer,
    BlogSerializer,
    BlogSingleSerializer
)


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSingleSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SubContentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubContent.objects.all()
    serializer_class = SubContentSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagBlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOrReadOnly]
