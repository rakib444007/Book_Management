from django.db import models
from User_profile.models import UserProfile
# Create your models here.


class Transactions(models.Model):
    account = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='account')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance_after_transaction = models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type = models.CharField(max_length=12,default="Deposite")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account.user.first_name

    class Meta:
        ordering = ['timestamp']   