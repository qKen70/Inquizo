from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, QuizAttachment
from .form import Quizform
from django.contrib.auth.models import User

def quizlist(request):
    quizo = Quiz.objects.all()
    return render(request, 'quizo/quizo_list.html', {'quizo': quizo})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizo/quiz_detail.html', {'quiz': quiz})

def addQuiz(request):
    if request.method != 'POST':
        form = Quizform()
    else:
        form = Quizform(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            quiz = form.save(commit=False)
            if not request.user.is_authenticated:
                quiz.author = User.objects.get(username='default_author')
            else:
                quiz.author = request.user
            quiz.save()
            for img in att:
                QuizAttachment.objects.create(quiz_id=quiz.pk, image=img)
            return redirect('quiz_detail', quiz_id=quiz.pk)

    return render(request, 'quizo/newquiz.html', {'form': form})

def editQuiz(request, pid):
    quiz = Quiz.objects.get(pk=pid)
    quiz_att = QuizAttachment.objects.filter(quiz_id=pid)
    if request.method != 'POST':
        form = Quizform(instance=quiz)
    else:
        form = Quizform(request.POST, instance=quiz)
        if form.is_valid():
            quiz = form.save(commit=False)
            att = request.FILES.getlist('images')
            for img in att:
                QuizAttachment.objects.create(quiz_id=quiz.pk, image=img)
            chosen = request.POST.getlist('attachments')
            for img_id in chosen:
                QuizAttachment.objects.get(pk=int(img_id)).delete()
            quiz.edited = True
            quiz.save()
        return redirect('quiz_detail', quiz_id=quiz.pk)

    return render(request, 'quizo/editquiz.html', {'form': form, 'quiz_att': quiz_att})

def deleteQuiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        quiz.delete()
        return redirect('quizlist')
    return render(request, 'quizo/delete_quiz.html', {'quiz': quiz})