from django.db import models


class State(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=218)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='region')

    def __str__(self):
        return f'{self.title}, {self.state.title}'


class Company(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=218)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=218)
    message = models.TextField()

    def __str__(self):
        return f"{self.email} subject: {self.subject}"
