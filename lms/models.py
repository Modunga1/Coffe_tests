from django.db import models
from django.contrib.auth.models import User


class MyModel(models.Model):
    my_field = models.TextField()


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    duration_weeks = models.PositiveIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=20)
    tags = models.ManyToManyField('Tag', blank=True)
    lecture_count = models.PositiveIntegerField(default=0)
    test_count = models.PositiveIntegerField(default=0)
    duration = models.PositiveIntegerField()  # Длительность курса в часах

    def __str__(self):
        return self.title

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    materials = models.FileField(upload_to='lecture_materials/')
    order = models.PositiveIntegerField(default=0)  # Порядок лекции в курсе

    def __str__(self):
        return self.title

class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    max_attempts = models.PositiveIntegerField(default=1)  # Максимальное количество попыток
    duration = models.PositiveIntegerField()  # Время на выполнение теста в минутах
    active = models.BooleanField(default=True)  # Активность теста

    def __str__(self):
        return self.title

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lectures = models.ManyToManyField(Lecture, blank=True)
    completed_tests = models.ManyToManyField(Test, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)  # Дата завершения курса
    progress = models.FloatField(default=0)  # Прогресс пользователя по курсу в процентах

    def __str__(self):
        return f'{self.user} - {self.course}'

class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'{self.user} - {self.test}'

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
