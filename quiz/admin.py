from django.contrib import admin
from .models import Quiz, Question, Answer, UserQuizResult


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ()
    ordering = ('title', 'author', '-created_at')  # Сортировка по названию, автору и дате (по убыванию)
    inlines = [QuestionInline]
    autocomplete_fields = ['author']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'created_at')
    search_fields = ('text',)
    list_filter = ()
    ordering = ('quiz', '-created_at')  # Сортировка по викторине и дате (по убыванию)
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ()
    ordering = ('question',)  # Сортировка по вопросу


class UserQuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completed_at')
    list_filter = ()
    search_fields = ('user__username',)
    ordering = ('-completed_at',)  # Сортировка по дате завершения (по убыванию)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserQuizResult, UserQuizResultAdmin)