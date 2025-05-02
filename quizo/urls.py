from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizlist, name='quizlist'),  # Список викторин
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),  # Детали викторины по ID
]