from rest_framework import serializers
from .models import Job, ApplyJob, Like


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'company', 'location', 'category',
                  'types', 'salary', 'working_day', 'tags', 'is_active', 'created_date']


class JobRetrieveSerializer(serializers.ModelSerializer):
    pass


class JobPostSerializer(serializers.ModelSerializer):
    pass
