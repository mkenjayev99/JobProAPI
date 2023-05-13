from django.db import models


class Job(models.Model):
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=218)
    position = models.ForeignKey('main.Position', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey('main.Company', on_delete=models.CASCADE)
    location = models.ForeignKey('main.City', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    tags = models.ManyToManyField('main.Tag')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    candidate = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='apply')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    message = models.TextField()

    def __str__(self):
        return f"{self.candidate} - {self.job}"


class Like(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
