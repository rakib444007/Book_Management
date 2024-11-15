from django.db import models
from django.contrib.auth.models import User
from User_profile.constants import GENDER_TYPE
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    initial_deposite_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    birth_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
