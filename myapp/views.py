from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
    langauges = Language.objects.all()
    return render(request, 'home.html', {'languages':langauges})

def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    return render(request, 'language_detail.html', {'language:':language, 'lesson':language.lesson.all()})

