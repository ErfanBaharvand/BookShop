from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return '%s , %s , %s' % (self.name, self.address, self.city)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return '%s , %s , %s' % (self.first_name, self.last_name, self.email)


class Category(models.Model):
    name = models.CharField(max_length=48, default="")
    en_name = models.CharField(max_length=48, default="")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    photo = models.ImageField(upload_to='book_images/')
    score = models.FloatField(max_length=5, default=0)
    categories = models.ManyToManyField(Category)
    chosen = models.BooleanField(default=False)
    description = models.CharField(max_length=512, default="")
    price = models.FloatField(default=0)

    def __str__(self):
        return '%s ,publisher %s' % (self.title, self.publisher)


class Slider(models.Model):
    title = models.CharField(max_length=48)
    number = models.IntegerField
    photo = models.ImageField(upload_to='Book/static/slider')
    enabled = models.BooleanField(default=False)
    description = models.CharField(max_length=128)
    book = models.ForeignKey(Book)

    def __str__(self):
        return 'slider %s, number %s,book %s' % (self.title, self.number, self.book)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return '%s, %s' % (self.user.first_name, self.user.last_name)


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return 'basket of user %s' % self.user