from django.db import models
from django.contrib.auth.models import User
from book_post.models import Book
# Create your models here.


class BorrowBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrow_user')
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrow_book')
    after_balance_borrow_book = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    borrow_book_date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f'user: {self.user} book: {self.book} borrow_date: {self.borrow_book_date}'