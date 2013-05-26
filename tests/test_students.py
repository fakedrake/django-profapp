import datetime
from django.test import TestCase
from django.test.client import Client

from profapp.models import Student

class TestStudent(TestCase):
    def setUp(self):
        self.c = Client()
        Student.objects.create(am=2222, first_name="Chris",
                        last_name="Perivolas",
                        date_enrolled=datetime.date(year=2010, day=15,
                                                    month=2))
        Student.objects.create(am=7362, first_name="Mary",
                        last_name="Karagewrgena",
                        date_enrolled=datetime.date(year=2010, day=15,
                                                    month=2))

    def test_list(self):
        r = self.c.get("/profapp/students/")
        self.assertIn("2222", r.content)
        self.assertIn("7362", r.content)

    def test_details(self):
        r = self.c.get("/profapp/students/2222/")
        self.assertIn("2222", r.content)
        self.assertIn("Chris", r.content)
        self.assertIn("Perivolas", r.content)

    def test_update(self):
        """
        """
        r = self.c.post("/profapp/students/2222/update/",
                        dict(am=7363, first_name="Chris",
                             last_name="Perivolas",
                             date_enrolled="3/15/2010",
                             semester=2,
                             undergraduate=1))

        self.assertRedirects(r, "/profapp/students/7363/")
        self.assertEquals(Student.objects.filter(am=7363).exists(), True)
        self.assertEquals(Student.objects.filter(am=2222).exists(), False)
