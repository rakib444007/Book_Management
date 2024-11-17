from django.shortcuts import render
from django.views.generic import ListView,FormView
from .forms import DepositForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

@method_decorator(login_required, name='dispatch')
class DepositeFormView(FormView):
    form_class = DepositForm
    template_name = 'transaction/deposite_form.html'
    success_url = reverse_lazy('user_deposite')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.user_profile
        })

        return kwargs


    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.user_profile
        account.balance += amount # amount = 200, tar ager balance = 0 taka new balance = 0+200 = 200
        account.save(
            update_fields=[
                'balance'
            ]
        )
        form.save()

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "transaction/deposite_email.html")
        return super().form_valid(form)

