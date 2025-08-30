from django.shortcuts import render
from .models import Teacher, Subject, Batch, Student

def dashboard(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    batches = Batch.objects.all()
    students = Student.objects.all()

    return render(request, "timetable/dashboard.html", {
        "teachers": teachers,
        "subjects": subjects,
        "batches": batches,
        "students": students,
    })
