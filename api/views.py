from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Language, Lesson, Vocabulary, QuizQuestion, Review, UserProgress
from .serializers import LanguageSerializer, LessonSerializer, VocabularySerializer, QuizQuestionSerializer, ReviewSerializer, UserProgressSerializer



@api_view(['GET', 'POST'])
def languages_list(request):
    if request.method == 'GET':
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def language_detail(request, pk):
    try:
        language = Language.objects.get(pk=pk)

    except Language.DoesNotExist:
        return Response({'error': 'Language not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = LanguageSerializer(language, data=request.data, partial=(request.method=='PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def lessons_list(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LessonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def lesson_detail_api(request, pk):
    try:
        lesson = Lesson.objects.get(pk=pk)

    except Lesson.DoesNotExist:
        return Response({'error': 'Lesson not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = LessonSerializer(lesson, data=request.data, partial=(request.method=='PATCH'))
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def vocab_list(request):
    if request.method == 'GET':
        vocabularies = Vocabulary.objects.all()
        serializer = VocabularySerializer(vocabularies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = VocabularySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vocab_detail(request, pk):
    try:
        vocab = Vocabulary.objects.get(pk=pk)
    except Vocabulary.DoesNotExist:
        return Response({'error': 'Vocabulary not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VocabularySerializer(vocab)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = VocabularySerializer(vocab, data=request.data, partial=(request.method=='PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vocab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
def quiz_list(request):
    if request.method == 'GET':
        questions = QuizQuestion.objects.all()
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = QuizQuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def quiz_detail(request, pk):
    try:
        question = QuizQuestion.objects.get(pk=pk)

    except QuizQuestion.DoesNotExist:
        return Response({'error': 'Quiz question not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizQuestionSerializer(question)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = QuizQuestionSerializer(question, data=request.data, partial=(request.method=='PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)

    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = ReviewSerializer(review, data=request.data, partial=(request.method=='PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
def progress_list(request):
    if request.method == 'GET':
        progress = UserProgress.objects.all()
        serializer = UserProgressSerializer(progress, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserProgressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def progress_detail(request, pk):
    try:
        progress = UserProgress.objects.get(pk=pk)

    except UserProgress.DoesNotExist:
        return Response({'error': 'User progress not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProgressSerializer(progress)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = UserProgressSerializer(progress, data=request.data, partial=(request.method=='PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
