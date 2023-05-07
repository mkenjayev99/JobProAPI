from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save


class Category(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=218)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/')

    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, author: {self.author}"


class SubImage(models.Model):
    image = models.ImageField(upload_to='blog/')


class SubContent(models.Model):
    title = models.CharField(max_length=218, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    images = models.ForeignKey(SubImage, on_delete=models.CASCADE)
    is_wide = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.author}'s comment ({self.id})"

    @property
    def get_related_comments(self):
        qs = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        if qs:
            return qs
        return None


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        top_level_comment = instance
        while top_level_comment.parent_comment:
            top_level_comment = top_level_comment.parent_comment
        instance.top_level_comment_id = top_level_comment.id
        instance.save()


post_save.connect(comment_post_save, sender=Comment)
