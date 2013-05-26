import datetime
from django.test import TestCase
from django.test.client import Client

from profapp.models import Student

class TestStudent(TestCase):
    def setUp(self):
        self.c = Client()
        Student.objects.create(am=7361, first_name="Chris",
                        last_name="Perivolas",
                        date_enrolled=datetime.date(year=2010, day=15,
                                                    month=2))
        Student.objects.create(am=7362, first_name="Mary",
                        last_name="Karagewrgena",
                        date_enrolled=datetime.date(year=2010, day=15,
                                                    month=2))

    def test_list(self):
        r = self.c.get("/profapp/students/")
        self.assertIn("7361", r.content)
        self.assertIn("7362", r.content)
