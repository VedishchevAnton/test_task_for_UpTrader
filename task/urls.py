from django.urls import path
from .views import MenuView

urlpatterns = [
    path('menu/<slug:slug>/', MenuView.as_view(), name='menu'),
]
