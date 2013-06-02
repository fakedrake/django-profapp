from django.db import models
from django.forms.extras.widgets import SelectDateWidget

EXAM_TYPES = (
    ('m', 'Midterm'),
    ('f', 'Final'),
    ('e', 'Excercise'),
    ('t', 'Test'),
)

class Student(models.Model):
    am = models.SmallIntegerField(unique=True) # XXX: max_value = 10000
    date_enrolled = models.DateField('Date Enrolled')
    semester = models.IntegerField(default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    undergraduate = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.am)


class SemesterSubject(models.Model):
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    unique_together = ('name','year')

    def __unicode__(self):
        return u"%s - %s" % (self.name, self.year)


class Exam(models.Model):
    subject = models.ForeignKey(SemesterSubject)
    type = models.CharField(max_length=15, choices=EXAM_TYPES)
    percent = models.FloatField()
    question_set = models.FileField(upload_to="files/")

    def __unicode__(self):
	EX_T = dict(EXAM_TYPES)
        return u"%s %s" % (self.subject.name, EX_T[self.type])

class Grade(models.Model):
    student = models.ForeignKey(Student)
    grade = models.IntegerField(default=0)
    exam = models.ForeignKey(Exam)

    def __unicode__(self):
        return self.exam.subject.name+" "+self.exam.type+" "+str(self.student.am)
