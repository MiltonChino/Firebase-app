from django.urls import path
from . import views

urlpatterns = [
    path("", views.firebase_detail, name="firebase_detail"),
]