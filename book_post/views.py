from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DetailView,CreateView,View
from django.contrib.auth.decorators import login_required
from .models import Book,BookReview
from .forms import BookReviewForm
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from category.models import Category
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from borrow_book.models import BorrowBook
from User_profile.models import UserProfile
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from transactions.models import Transactions

# Create your views here.
def send_transaction_email(user, amount, subject, template,book=None):
        message = render_to_string(template, {
            'user' : user,
            'book' : book,
        })

        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


class BookPostView(ListView):
    model = Book
    template_name = 'post/bookpost.html'
    context_object_name = 'dt'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = super().get_queryset()
        if slug:
            book_cat = get_object_or_404(Category,slug = slug)
            queryset = queryset.filter(Category=book_cat)
        return queryset
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "post/book_details.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        user = self.request.user
        context["can_borrow"] = user.is_authenticated and not BorrowBook.objects.filter(user=user,book=book)
        context["can_review"] = user.is_authenticated and BorrowBook.objects.filter(user=user, book=book).exists()
        context["review_form"] = BookReviewForm()  # Include review form
        return context


class BookReviewView(LoginRequiredMixin, CreateView):
    model = BookReview
    form_class = BookReviewForm
    template_name = "post/book_details.html"  
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = get_object_or_404(Book, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("book_detail", kwargs={"pk": self.kwargs["pk"]})




class BorrowBookView(LoginRequiredMixin, View):

    
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user_profile = UserProfile.objects.get(user=request.user)
        
        if user_profile.balance < book.BookPrice:
            messages.warning(request, "You do not have enough balance to borrow this book.You should deposite enough money in your account to buy this book.")
            return redirect('book_detail', pk=book.id)  

        if not BorrowBook.objects.filter(user=request.user, book=book).exists():
            user_profile.balance -= book.BookPrice
            BorrowBook.objects.create(
                user=request.user,
                book=book,
                after_balance_borrow_book = user_profile.balance 
            )

            
            user_profile.save(update_fields=['balance'])
            Transactions.objects.create(
                account = user_profile,
                amount = book.BookPrice,
                balance_after_transaction=user_profile.balance,
                transaction_type ='BorrowedBook'
            )
            send_transaction_email(request.user,book.BookPrice,"Borrowed Book",'post/book_borrow_email.html',book.title)
            messages.success(request, "You have successfully borrowed the book!")
       
        return redirect('book_detail', pk=book.id)


    