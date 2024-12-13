from django.contrib import admin
from .models import Teacher, Student, Subject, Class, Assignment, Submission, Attendance, Exam, ExamResult, AdministrativeStaff

# Registering models
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(AdministrativeStaff)
