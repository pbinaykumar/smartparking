# urls.py

from django.urls import path
from .views import SlotListView

urlpatterns = [
    path('get-slots/', SlotListView.as_view()),
]
