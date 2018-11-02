from django.views.generic import TemplateView
from django.shortcuts import render

class AccountsView(TemplateView):
    template_name = 'accounts/login.html'
