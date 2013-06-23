import datetime
from django.test import TestCase
from django.test.client import Client

from profapp.models import Grade, Student, Exam, SemesterSubject


MIN_AM_RANGE = 1000
MAX_AM_RANGE = 1100

class TestGrades(TestCase):
    def setUp(self):
        self.c = Client()

	self.subj = SemesterSubject(name="Math", year=2010)
	self.subj.save()
	self.subj.students.add(*[Student.objects.create(am=i,
                                           date_enrolled=datetime.datetime.now(),
                                           semester=1,
                                           first_name="Chodey",
                                           last_name="McNumnuts") for i in xrange(MIN_AM_RANGE,MAX_AM_RANGE)])
	self.subj.save()

	self.stu = self.subj.students.all()

        self.exam1 = Exam.objects.create(subject=self.subj, type='m', percent=20)
	self.exam2 = Exam.objects.create(subject=self.subj, type='f', percent=30)

        self.grds1 = [Grade.objects.create(student=s, grade=5, exam=self.exam1) for s in self.stu]
	self.grds2 = [Grade.objects.create(student=s, grade=6, exam=self.exam2) for s in self.stu]

    def test_list_grades(self):
	r = self.c.get("/profapp/grades/")

	# Assert that all students were graded
	for am in xrange(MIN_AM_RANGE, MAX_AM_RANGE):
	    self.assertIn(str(am), r.content)

	self.assertIn("Final", r.content)
	self.assertIn("Midterm", r.content)

    def test_list_get(self):
	r = self.c.get("/profapp/grades/?exam=%s" % self.exam1.pk)
	self.assertNotIn(self.exam2.get_type_display(), r.content)

	r = self.c.get("/profapp/grades/?stud=%s" % self.stu[0].pk)
        for s in self.stu[1:]:
            self.assertNotIn("<td>%s</td>" % s.am, r.content)

        self.assertIn("<td>%s</td>" % self.stu[0].am, r.content)
