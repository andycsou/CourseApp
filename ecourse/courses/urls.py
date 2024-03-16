from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('courses/', views.index, name="index"),
    path('courses/<int:course_id>', views.list, name="list"),
    path('category/', views.CategoryView.as_view()),
]
