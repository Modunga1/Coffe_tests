from django.shortcuts import render
from .models import Lecture
from .models import Course
from django.http import HttpResponse

def lecture_detail(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})

def home(request):
    return render(request, 'home.html')

def course_detail(request, course_id):
    # Получаем курс по его идентификатору
    course = Course.objects.get(pk=course_id)

    # Создаем фиктивные данные для отображения на странице
    lecture_progress = 50  # Пример значения прогресса лекций (в процентах)
    test_progress = 70  # Пример значения прогресса тестов (в процентах)

    # Передаем данные в шаблон
    return render(request, 'course_detail.html', {'course': course, 'lecture_progress': lecture_progress, 'test_progress': test_progress})

