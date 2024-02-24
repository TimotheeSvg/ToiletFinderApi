
from django.contrib import admin
from django.urls import path
from toilet import views

urlpatterns = [
    path('toilet/', views.ToiletView.as_view()),
]
