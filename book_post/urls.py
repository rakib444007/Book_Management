
from django.urls import path
from .views import BookPostView,BookDetailView, BorrowBookView, BookReviewView

urlpatterns = [
    path('', BookPostView.as_view(),name='homepage'),
    path('book_post/', BookPostView.as_view(),name='book_post'),
    path('book_post_category_wise/<slug:slug>', BookPostView.as_view(),name='category_wise_post'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/review/', BookReviewView.as_view(), name='book_review_create'),
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow_book'),
]