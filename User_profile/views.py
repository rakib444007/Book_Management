
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserResgistrationsForm
from django.views.generic import FormView,ListView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from borrow_book.models import BorrowBook,Book
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages
from .models import UserProfile




class UserRegistrationView(FormView):
    template_name ='registration_form.html'
    form_class =UserResgistrationsForm
    success_url = reverse_lazy('register')


    def form_valid(self,form):
        user = form.save()
        print(user)
        login(self.request,user)
        return super().form_valid(form)


# Create your views here.



class UserLoginView(LoginView):
    template_name ='user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    



def Userlogout(request):
    logout(request)
    return redirect('homepage')


    

class ReturnBorrowBook(LoginRequiredMixin,View):
    def post(self,request,book_id):
        book = get_object_or_404(Book,id = book_id)
        borrowed_book = BorrowBook.objects.get(user=request.user,book = book)
        if borrowed_book:
            borrowed_book.delete()
            messages.success(request,'The borrowed book has been returned successfully.')

            user = UserProfile.objects.get(user=request.user)
            user.balance += book.BookPrice
            user.save(
                update_fields=[
                    'balance'
                ]
            )
        else:
            messages.error(request,'This borrowed book record does not exit!!')

        return redirect('profile')



class BorrowReportView(LoginRequiredMixin,ListView):
    model = BorrowBook
    template_name='profile.html'
    context_object_name='borrow_details'

    def get_queryset(self) :
        queryset = super().get_queryset().filter(
            user = self.request.user
        )         
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance_user = UserProfile.objects.get(user = self.request.user)
        context["Userbalance"] =  instance_user.balance
      
        return context
    

