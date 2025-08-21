from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('languages/<int:pk>/', views.language_detail, name = 'language_detail'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/quiz/', views.quiz_view, name='quiz_view'),
    path('lessons/<int:lesson_id>/quiz/result/', views.quiz_result, name='quiz_result'),
    path('signup/', views.sign_up, name='sign_up'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.log_out, name='log_out')
]