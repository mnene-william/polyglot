from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__ (self):
        return self.name
    
class Lesson(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveBigIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__ (self):
        return f"{self.language.name} - {self.title}"
    
class Vocabulary(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="vocab")
    word = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)

    def __str__ (self):
        return f"{self.word} = {self.translation}"
    
class QuizQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)

    def __str__ (self):
        return f"Q: {self.question_text[:100]}"
    
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("user", "lesson")

    def __str__ (self):
        return f"{self.user.username} - {self.lesson.title} - {self.score}"
    

class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='reviews')

    def __str__ (self):
        return f'Review by {self.author} for {self.language}'


    


