from django.urls import path
from .views import student_list, add_student  # ✅ Ensure these functions exist in views.py

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('add_student/', add_student, name='add_student'),
]
