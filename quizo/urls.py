from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizlist, name='quizlist'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('add/', views.addQuiz, name='add_quiz'),
    path('<int:pid>/edit/', views.editQuiz, name='edit_quiz'),
    path('<int:pid>/delete/', views.deleteQuiz, name='delete_quiz'),
]