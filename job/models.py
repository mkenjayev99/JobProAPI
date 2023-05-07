from django.db import models
from main.models import Category, Tag, Type, Company, City
from account.models import Account


class Job(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=218)
    position = models.ForeignKey('main.Position', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type)
    salary = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    working_day = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    candidate = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='apply')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate} - {self.job}"


class Like(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)


