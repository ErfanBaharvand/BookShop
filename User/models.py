from django.contrib.auth.models import User
from django.db import models

from Book.models import Book


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return '%s, %s' % (self.user.first_name, self.user.last_name)


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return 'basket of user %s' % self.user
