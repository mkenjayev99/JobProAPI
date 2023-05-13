from django.db.models import Q
from rest_framework import generics, permissions, serializers
from .models import Job, ApplyJob, Like
from .serializers import (JobRetrieveSerializer,
                          JobPostSerializer,
                          JobSerializer,
                          LikeSerializer,
                          ApplyJobSerializer,
                          ApplyJobGetSerializer)


class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        cat = self.request.GET.get('cat')
        location = self.request.GET.get('location')
        search_condition = Q()
        cat_condition = Q()
        location_condition = Q()
        if search:
            search_condition = Q(title__icontains=q)
        if cat:
            cat_condition = Q(category__title__exact=cat)
        if location:
            location_condition = Q(ciy_title__icontains=location)
        qs = qs.filter(search_condition, cat_condition, location_condition)
        return qs


class JobPostAPIView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobRetrieveSerializer


class LikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        candidate_id = self.request.user.id
        return qs.filter(candidate_id=candidate_id)


class ApplyJobListCreateAPIView(generics.ListCreateAPIView):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplyJobListAPIView(generics.ListAPIView):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobGetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):  # function checks the user if he is candidate or HR.
        qs = super().get_queryset()
        candidate = self.request.user
        if not candidate.role == 2:
            raise PermissionError('You are not HR!')
        job_id = self.kwargs.get('job_id')
        if candidate.role == 1:
            raise serializers.ValidationError('You are not HR!')
        return qs.filter(job_id=job_id)
