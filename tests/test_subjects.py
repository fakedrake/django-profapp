import datetime
from django.test import TestCase
from django.test.client import Client

from profapp.models import Student

class TestStudent(TestCase):
    def setUp(self):
        self.stu = [Student.objects.create(am=i,
                                           date_enrolled=datetime.datetime.now(),
                                           semester=1,
                                           first_name="Chodey",
                                           last_name="McNumnuts") for i in xrange(1000,1010)]

        subj = SemesterSubject.objects.create(students=self.stu, name="Math", year=2010)
