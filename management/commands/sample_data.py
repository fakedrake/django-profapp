import datetime
import random

import django.db as db
from django.core.management.base import NoArgsCommand, make_option

from profapp.models import Grade, Student, Exam, SemesterSubject, EXAM_TYPES

def sqlverbose(func):
    def new_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        for q in db.connection.queries:
            print q["sql"]

        return ret

    return new_func


def random_partition(k, iterable):
    results = [[] for i in range(k)]
    for value in iterable:
        x = random.randrange(k)
        results[x].append(value)

    return results

@sqlverbose
def create_students(min_am, max_am):
    """
    Create an enormous family of students.
    """
    ret = []

    for i in xrange(min_am, max_am):
        if not Student.objects.filter(am=i).exists():
            st = Student.objects.create(am=i,
                                        date_enrolled=datetime.datetime.now(),
                                        semester=i%10,
                                        first_name="Chodey%d" % (i - min_am),
                                        last_name="McNumnuts")
        else:
            st = Student.objects.get(am=i)

        ret.append(st)

    return ret


@sqlverbose
def create_subjects(students, k):
    """
    Create subjects witht eh students in them.
    """
    ret = []
    stud_set = random_partition(k, students)
    for i in xrange(k):
        s_name = "Subject %d" % (i/13)
        s_year = 2000 + i%13

        if SemesterSubject.objects.filter(name=s_name, year=s_year).exists():
            subj = SemesterSubject.objects.get(name=s_name, year=s_year)
        else:
            subj = SemesterSubject(name=s_name, year=s_year)
            subj.save()
            subj.students.add(*stud_set[i])
            subj.save()

        ret.append(subj)

    return ret

@sqlverbose
def create_exams(subjects):
    """
    Create a couple of exams for each subjects.
    """
    ret = []

    for s in subjects:
        for t in xrange(random.randrange(len(EXAM_TYPES))):
            tmp = random.randrange(len(EXAM_TYPES))
            e_type = EXAM_TYPES[tmp][0]
            e_prc = 100/len(EXAM_TYPES)*tmp

            if Exam.objects.filter(subject=s, type=e_type, percent=e_prc).exists():
                exam = Exam.objects.get(subject=s, type=e_type, percent=e_prc)
            else:
                exam = Exam.objects.create(subject=s, type=e_type, percent=e_prc)

            ret.append(exam)

    return ret

@sqlverbose
def create_grades(students):
    """
    Create some grades for each student.
    """
    ret = []
    for s in students:
        exams = Exam.objects.filter(subject__students=s)
        for e in random_partition(2, exams)[0]:
            # Get a couple of random exams that are available.
            if Grade.objects.filter(student=s, grade=random.randrange(10), exam=e).exists():
                grade = Grade.objects.get(student=s, grade=random.randrange(10), exam=e)
            else:
                grade = Grade.objects.create(student=s, grade=random.randrange(10), exam=e)

            ret.append(grade)

    return ret

class Command(NoArgsCommand):

    help = "Fill the database with sample data."

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )

    def handle_noargs(self, **options):
        stu = create_students(1000, 1100)
        subj = create_subjects(stu, 20)
        ex = create_exams(subj)
        grds = create_grades(stu)
