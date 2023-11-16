# urls.py

from django.urls import path
from .views import UserSignupView,UserSigninView

urlpatterns = [
    path('signup/', UserSignupView.as_view()),
    path('signin/', UserSigninView.as_view(), name='signin'),
]
