from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='book_post/upload',blank=True,null=True)
    BookPrice = models.DecimalField(max_digits=10,decimal_places=2)
    Category = models.ManyToManyField(Category, related_name='BookCategory')

    def __str__(self):
        return self.title


class BookReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='book_review')
    review = models.TextField()
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} book: {self.book}'
    
    