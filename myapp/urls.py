from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('languages/<int:pk>/', views.language_detail, name = 'language_detail'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/quiz/', views.quiz_view, name='quiz'),
    path('lessons/<int:lesson_id>/quiz/result/', views.quiz_result, name='quiz_result'),
    path('signup/', views.sign_up, name='signup')
]