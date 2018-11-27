from django.conf.urls import url
from .views import AccountsView, SignUp
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url('register/', SignUp.as_view(template_name="accounts/register.html"), name='signup'),
]