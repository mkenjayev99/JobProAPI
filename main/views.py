from rest_framework import permissions
from account.permissions import IsAdminUserOrReadOnly
from rest_framework import generics
from .models import Subscribe, Contact, Category, Tag, Position, Company
from .serializers import (ContactSerializer,
                          CategorySerializer,
                          TagSerializer,
                          PositionSerializer,
                          CompanySerializer,
                          SubscribeSerializer
                          )


class SubscribePostView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactPostView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagListCreateApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PositionListCreateApiView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CompanyListCreateApiView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
