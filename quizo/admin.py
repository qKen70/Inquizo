from django.contrib import admin
from .models import Quiz, Question, Answer, UserQuizResult, QuizAttachment
from django.contrib.auth import get_user_model

User = get_user_model()

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuizAttachmentInline(admin.TabularInline):
    model = QuizAttachment
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('title', 'author', '-created_at')
    inlines = [QuestionInline, QuizAttachmentInline]
    autocomplete_fields = ['author']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'created_at')
    search_fields = ('text',)
    ordering = ('quiz', '-created_at')
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    ordering = ('question',)

class UserQuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completed_at')
    search_fields = ('user__email',)
    ordering = ('-completed_at',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserQuizResult, UserQuizResultAdmin)
admin.site.register(QuizAttachment)