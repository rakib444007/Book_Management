
from django.urls import path
from .views import UserRegistrationView,UserLoginView,Userlogout,ReturnBorrowBook,BorrowReportView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('user_login/',UserLoginView.as_view(),name='user_login'),
    path('user_logout/',Userlogout,name='user_logout'),
    path('return/book/<int:book_id>/',ReturnBorrowBook.as_view(),name='book_return'),
    path('profile/',BorrowReportView.as_view(),name='profile'),
]
