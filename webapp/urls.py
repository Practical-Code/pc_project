from django.conf.urls import url
from .views import WebAppView

urlpatterns = [
    url(r'^$', WebAppView.as_view()),
]