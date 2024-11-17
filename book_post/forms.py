
# forms.py
from django import forms
from .models import BookReview

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={
                'class': 'w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Write your review...'
            }),
            'rating': forms.Select(choices=[(i, f"{i}") for i in [1, 2, 3, 4, 5]], attrs={
                'class': 'mt-2 w-full p-2 border rounded-lg',
            }),
        }
