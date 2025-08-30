from django.contrib import admin
from .models import Teacher, Subject, Batch, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "branch")
    list_filter = ("branch",)
    search_fields = ("name",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "teacher")
    list_filter = ("branch",)
    search_fields = ("name", "teacher__name")

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("name", "subject")
    search_fields = ("name", "subject__name")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "roll_no", "branch", "batch")
    list_filter = ("branch", "batch")
    search_fields = ("name", "roll_no")
