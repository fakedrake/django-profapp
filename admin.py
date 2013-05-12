from django.contrib import admin
from profapp.models import Student, SemesterSubject, Exam, Grade

admin.site.register(Student)
admin.site.register(SemesterSubject)
admin.site.register(Exam)
admin.site.register(Grade)
