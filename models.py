from django.db import models
from django.forms.extras.widgets import SelectDateWidget

EXAM_TYPES = (
    ('m', 'midterm'),
    ('f', 'final'),
    ('e', 'excercise'),
    ('t', 'test'),
)

class Student(models.Model):
    am = models.SmallIntegerField(unique=True, primary_key=True) # XXX: max_value = 10000
    date_enrolled = models.DateField('Date Enrolled')
    semester = models.IntegerField(default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    undergraduate = models.BooleanField()

class SemesterSubject(models.Model):
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=100)
    year = models.IntegerField()

class Exam(models.Model):
    subject = models.ForeignKey(SemesterSubject)
    type = models.CharField(max_length=1, choices=EXAM_TYPES)
    percent = models.FloatField()
    question_set = models.FileField(upload_to="files/")

class Grade(models.Model):
    student = models.ForeignKey(Student)
    grade = models.IntegerField(default=0)
    exam = models.ForeignKey(Exam)
