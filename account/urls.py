from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.AccountRegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

    path('list/', views.AccountListAPIView.as_view()),
    path('rud/<int:pk>/', views.AccountRUDAPIView.as_view()),
]

