from django.conf.urls import url
from .views import AccountsView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
]