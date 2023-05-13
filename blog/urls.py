from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.BlogListCreateAPIView.as_view()),
    path('rud/<int:pk>/', views.BlogRUDAPIView.as_view()),
    path('subcontent/rud/<int:pk>/', views.SubContentRUDAPIView.as_view()),

    path('category/list-create/', views.CategoryListCreateAPIView.as_view()),

    path('tag/rud/<int:pk>/', views.TagRUDAPIView.as_view()),

    path('comment/create/<int:pk>/', views.CommentCreateAPIView.as_view()),
    path('comment/rud/<int:pk>/', views.CommentRUDAPIView.as_view()),
]
