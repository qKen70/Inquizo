# quizo/views.py
from django.shortcuts import render, get_object_or_404
from .models import Quiz

def quizlist(request):
    quizo = Quiz.objects.all()
    return render(request, 'quizo/quizo_list.html', {'quizo': quizo})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)  # Получаем викторину по ID или 404, если не найдена
    return render(request, 'quizo/quiz_detail.html', {'quiz': quiz})