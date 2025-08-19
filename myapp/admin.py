from django.contrib import admin
from .models import Language, Lesson, Vocabulary, QuizQuestion, UserProgress

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name","code")
    search_fields = ("name","code")

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title","language","order")
    list_filter = ("language",)
    ordering = ("language","order")

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ("word","translation","lesson")
    search_fields = ("word","translation")

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","lesson")
    list_filter = ("lesson",)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user","lesson","score","completed","updated_at")
    list_filter = ("completed","lesson")


# Register your models here.
