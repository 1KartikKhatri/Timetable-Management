from django.db import models

BRANCHES = [
    ('CSE', 'Computer Science & Engineering'),
    ('ECE', 'Electronics & Communication Engineering'),
    ('EE', 'Electrical Engineering'),
]

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=10, choices=BRANCHES)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.branch})"

class Batch(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.subject.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=10, choices=BRANCHES)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
