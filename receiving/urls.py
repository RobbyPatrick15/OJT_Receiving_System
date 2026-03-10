from django.urls import path
from . import views

urlpatterns = [
    path('', views.receiving_view, name='receiving'),
]