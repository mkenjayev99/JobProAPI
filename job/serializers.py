from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Job, ApplyJob, Like
from main.serializers import CompanySerializer, CategorySerializer, TagSerializer, PositionSerializer
from account.serializers import AccountSerializer


class JobSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    author = AccountSerializer(read_only=True)
    tags = TagSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'company', 'category', 'position', 'salary', 'tags']


class JobRetrieveSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'position', 'company', 'location', 'category',
                  'salary', 'tags', 'is_active', 'created_date']


class JobPostSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'salary', 'company', 'tags']

    def validate(self, attrs):
        request = self.context['request']
        author = request.user
        if author.role == request.user:
            raise ValidationError("You don't have permission")
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        author = request.user
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class LikeSerializer(serializers.ModelSerializer):
    job = JobRetrieveSerializer(read_only=True)
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'author', 'job']


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = ['id', 'candidate', 'resume', 'message']
        extra_kwargs = {
            'candidate': {'required': False}
        }

        @staticmethod
        def validate(attrs):
            candidate = attrs.get('candidate')
            if not candidate.role == 1:
                raise ValidationError('You are not candidate!')
            return attrs


class ApplyJobGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = ['candidate', 'job', 'resume', 'message']
