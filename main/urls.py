from django.urls import path
from . import views

urlpatterns = [
    path('subscribe-post/', views.SubscribePostView.as_view()),
    path('contact-post/', views.ContactPostView.as_view()),

    path('category-list-create/', views.CategoryListCreateAPIView.as_view()),
    path('tag-list-create/', views.TagListCreateApiView.as_view()),

    path('position-list-create/', views.PositionListCreateApiView.as_view()),
    path('company-list-create/', views.CompanyListCreateApiView.as_view()),
]
