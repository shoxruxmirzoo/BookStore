from django.db import models


# Create your models here.

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=36, null=False, blank=False, default='')

    description = models.TextField(blank=True, max_length=256)

    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)

    published = models.DateField(default=None, blank=True, null=True)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    books = models.ManyToManyField(Book, related_name='author')
