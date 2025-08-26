from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    languages = Language.objects.all()
    reviews = Review.objects.all()

    languages_images = {
        'Swahili': 'images/france.png',
        'French': 'images/france.png',

    }

    context = {
        'languages': languages,
        'reviews': reviews,
        'languages_images': languages_images,
    }

    return render(request, 'home.html', context)
     
@login_required
def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)

    lessons = language.lessons.all()

    return render(request, 'language_detail.html', {'language':language, 'lessons': lessons})


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    vocabularies = lesson.vocab.all()

    return render(request, 'lesson_detail.html', {'lesson': lesson, 'vocabularies': vocabularies})


@login_required
def quiz_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    questions = lesson.questions.all()

    total_questions = questions.count()

    quiz_state = request.session.get('quiz_state', {})

    

    
    
    if 'q_index' not in request.session or request.GET.get('restart'):
        request.session['q_index'] = 0
    
        request.session['score'] = 0

        question_ids = list(lesson.questions.values_list('id', flat=True))

        request.session['question_ids'] = question_ids
        request.session['feedback'] = None


    index = request.session['q_index']

    question_ids = request.session.get('question_ids', [])

    if request.GET.get('next_question'):
        request.session['q_index'] += 1
        request.session['feedback'] = None
        return redirect('quiz_view', lesson_id=lesson.id)


    if index >= len(question_ids):

        return redirect('quiz_result', lesson_id= lesson.id)
    
    question = QuizQuestion.objects.get(id=request.session['question_ids'][index])

    if request.method == 'POST':
        selected = request.POST.get('answer')

        is_correct = selected and selected.strip() == question.correct_answer.strip()

        request.session['feedback'] = {
            'is_correct': is_correct,
            'user_selected': selected,
            'correct_answer': question.correct_answer
        }

        if is_correct:
            request.session['q_index'] = index + 1

        return redirect('quiz_view', lesson_id=lesson.id)
    
    feedback = request.session.get('feedback')

    context = {
        'lesson': lesson,
        'question': question,
        'index': index + 1,
        'total': len(question_ids),
        'feedback': feedback,
    }

    return render(request, 'quiz_view.html', context)




@login_required
def quiz_result(request, lesson_id):

    lesson  = get_object_or_404(Lesson, pk=lesson_id)

    score = request.session.get('score', 0)

    total = len(request.session.get('question_ids', []))


    up, created = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)

    up.score = int(score / max(total, 1) * 100)
    
    up.completed = True

    up.save()


    for key in ('q_index', 'score', 'question_ids'):

        request.session.pop(key, None)

    return render(request, 'quiz_result.html', {'lesson': lesson, 'score': score, 'total':total, 'percent': up.score})




def sign_up(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')



def submit_review(request):

    languages = Language.objects.all()

    if request.method == 'POST':

        author = request.POST.get('author')
        text = request.POST.get('review_text')
        rating = request.POST.get('rating')

        language_id = request.POST.get('language')
          
        if author and text and rating and language_id:
          try:

            rating = int(rating)

            all_languages = get_object_or_404(Language, pk=language_id)

            Review.objects.create(author=author, text=text, rating=rating, language=all_languages)

            messages.success(request, 'Thank you for Review!It has been submitted successfully!')

            return redirect('home')

          except:
              messages.error(request, 'Invalid form submission. Please enter a number between 1 and 5')
              languages  = Language.objects.all()
              
              return render(request, 'review.html')
             
        
        else:
            messages.error(request, 'All fields are required.')
            languages  = Language.objects.all()

    return render(request, 'review.html', {'languages':languages})

@login_required
def user_profile(request):
 


    user_progress_entries = UserProgress.objects.filter(user=request.user)
    

    completed_lessons_count = user_progress_entries.filter(completed=True).count()
    

    total_lessons_count = Lesson.objects.all().count()
    

    progress_percentage = 0
    if total_lessons_count > 0:
        progress_percentage = int((completed_lessons_count / total_lessons_count) * 100)


    completed_lessons_list = [
        {
            'title': entry.lesson.title,
            'language': entry.lesson.language.name  
        } 
        for entry in user_progress_entries.filter(completed=True)
    ]

    context = {
        'user': request.user,
        'completed_lessons_count': completed_lessons_count,
        'total_lessons_count': total_lessons_count,
        'progress_percentage': progress_percentage,
        'completed_lessons_list': completed_lessons_list,
    }
    
    return render(request, 'userprofile.html', context)


