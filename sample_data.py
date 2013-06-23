from profapp.models import Grade, Student, Exam, SemesterSubject, EXAM_TYPES

def random_partition(k, iterable):
    results = [[] for i in range(k)]
    for value in iterable:
        x = random.randrange(k)
        results[x].append(value)

    return results

def create_students(min_am, max_am):
    """
    Create an enormous family of students.
    """
    return [Student.objects.create(am=i,
                                   date_enrolled=datetime.datetime.now(),
                                   semester=i%10,
                                   first_name="Chodey%d" % i - min_amx,
                                   last_name="McNumnuts") for i in xrange(min_am, max_am)]


def create_subjects(students, k):
    """
    Create subjects witht eh students in them.
    """
    ret = []
    stud_set = random_partition(k, students)
    for i in k:
        subj = SemesterSubject(name="Subject %d" % i, year=2000+i%13)
        subj.save()
        subj.students.add(*stud_set[i])
        subj.save()
        ret.append(subj)

    return ret

def create_exams(subjects):
    """
    Create a couple of exams for each subjects.
    """
    ret = []

    for s in subjects:
        for t in xrange(random.randrange(len(EXAM_TYPES))):
            tmp = random.randrange(len(EXAM_TYPES))
            ret.append(Exam.objects.create(subject=s, type=EXAM_TYPES[tmp][0], percent=100/len(EXAM_TYPES)*tmp))

    return ret

def create_grades(subjects):
    """
    Create some grades for each student.
    """
    ret = []
    for s in students:
        exams = Exams.objects.filter(exam__subject__students__in=s)
        for e in random_partition(2, exams)[0]:
            # Get a couple of random exams that are available.
            ret.append(Grade.objects.create(student=s, grade=random.randrange(10), exam=e))

    return ret


stu = create_students(1000, 1100)
subj = create_subjects(stu, 20)
ex = create_exams(subj)
grds = create_grades(subj)
