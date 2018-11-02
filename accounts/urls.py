from django.conf.urls import url
from .views import AccountsView
from django.contrib.auth import login

urlpatterns = [
    url(r'^$', AccountsView.as_view()),
]