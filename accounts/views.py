from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class AccountsView(TemplateView):
    template_name = 'accounts/login.html'

class SignUp(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')