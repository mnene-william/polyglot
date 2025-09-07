from django.urls import path
from . import views

urlpatterns = [
    path('languages/', views.languages_list, name='languages-list'),
    path('languages/<int:pk>/', views.language_detail, name='language-detail'),

    path('lessons/', views.lessons_list, name='lessons-list'),
    path('lessons/<int:pk>/', views.lesson_detail_api, name='lesson-detail'),

    path('vocab/', views.vocab_list, name='vocab-list'),
    path('vocab/<int:pk>/', views.vocab_detail, name='vocab-detail'),

    path('quiz/', views.quiz_list, name='quiz-list'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz-detail'),

    path('reviews/', views.reviews_list, name='review-list'),
    path('reviews/<int:pk>/', views.review_detail, name='review-detail'),

    path('progress/', views.progress_list, name='progress-list'),
    path('progress/<int:pk>/', views.progress_detail, name='progress-detail'),
    
]