from django.urls import path
from . import views

urlpatterns = [
        path('job-list/', views.JobListAPIView.as_view()),
        path('job-post/', views.JobPostAPIView.as_view()),
        path('job-rud/', views.JobRUDAPIView.as_view()),

        path('job-list-create/', views.LikeListCreateAPIView.as_view()),

        path('applyjob-list-create/', views.ApplyJobListCreateAPIView.as_view()),
        path('applyjob-list/', views.ApplyJobListAPIView.as_view()),
]

