from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField("Название викторины", max_length=255)
    description = models.TextField("Описание", blank=True)
    cover = models.ImageField("Обложка", upload_to='quiz_covers/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes', verbose_name="Автор")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Викторина"
        verbose_name_plural = "Викторины"

    def save(self, *args, **kwargs):
        # Убираем изменение поля title на имя файла
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name="Викторина")
    text = models.TextField("Вопрос")
    image = models.ImageField("Картинка к вопросу", upload_to='question_images/', blank=True, null=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def save(self, *args, **kwargs):
        # Убираем изменение поля text на имя файла картинки
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name="Вопрос")
    text = models.CharField("Ответ", max_length=255)
    is_correct = models.BooleanField("Правильный ответ", default=False)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.text} ({'Верный' if self.is_correct else 'Неверный'})"

class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_results', verbose_name="Пользователь")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results', verbose_name="Викторина")
    score = models.IntegerField("Счёт")
    completed_at = models.DateTimeField("Дата прохождения", auto_now_add=True)

    class Meta:
        verbose_name = "Результат пользователя"
        verbose_name_plural = "Результаты пользователей"

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score})"