from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
    langauges = Language.objects.all()
    return render(request, 'home.html', {'languages':langauges})

def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    return render(request, 'language_detail.html', {'language:':language, 'lesson':language.lessons.all()})


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    return render(request, 'lesson_detail.html', {'lesson': lesson, 'vocab': lesson.vocab.all()})


@login_required
def quiz_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    question_ids = list(lesson.questions.values_list('id'))
    
    if 'q_index' not in request.session or request.GET.get('restart'):
        request.session['q_index'] = 0
    
        request.session['score'] = 0

        request.session['question_ids'] = question_ids


    index = request.session['q_index']

    if index >= len(question_ids):

        return redirect('quiz_result', lesson_id= lesson.id)
    
    question = QuizQuestion.objects.get(id=request.session['question_ids'][index])

    if request.method == 'POST':
        selected = request.POST.get('answer')

        if selected and selected.strip() == question.correct_answer.strip():

            request.session['score'] += 1

        request.session['q_index'] = index + 1

        return redirect('quiz', lesson_id=lesson.id)
    
    return render(request, 'quiz.html', {'lesson':lesson, 'question': question, 'index': index+1, 'total': len(question_ids)})


@login_required
def quiz_result(request, lesson_id):

    lesson  = get_object_or_404(Lesson, pk=lesson_id)

    score = request.session.get('score', 0)

    total = len(request.session.get('question_ids', []))


    up = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)

    up.score = int(score / max(total, 1) * 100)
    
    up.completed = True

    up.save()


    for key in ('q_index', 'score', 'question_ids'):

        request.session.pop(key, None)

    return render(request, 'quiz_result.html', {'lesson': lesson, 'score': score, 'total':total, 'percent': up.score})


