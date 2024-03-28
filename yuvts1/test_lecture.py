from yuvts2 import Lecture


def test_add_student():
    lecture = Lecture("Diskret", "MATH202")
    lecture.add_student("Taivanbat")
    assert "Taivanbat" in lecture.students
    assert lecture.students["Taivanbat"] is None


def test_add_grade():
    lecture = Lecture("Physics", "PHYS101")
    lecture.add_student("Taivanbat")
    lecture.add_grade("Taivanbat", 88)
    assert lecture.students["Taivanbat"] == 88


def test_get_total_students():
    lecture = Lecture("History of Art", "ART101")
    lecture.add_student("Taivanbat")
    lecture.add_student("Taivan")
    assert lecture.get_total_students() == 2


def test_get_all_students_total_average():
    lecture = Lecture("Computer Science", "CS101")
    lecture.add_student("Taivanbat")
    lecture.add_student("Taivan")
    lecture.add_grade("Taivanbat", 92)
    lecture.add_grade("Taivan", 88)
    assert lecture.get_all_students_total_average() == 90


def test_get_all_students_total_average_with_ungraded_students():
    lecture = Lecture("Biology 101", "BIO101")
    lecture.add_student("Taivanbat")
    lecture.add_student("Taivan")
    lecture.add_grade("Taivanbat", 95)
    assert lecture.get_all_students_total_average() == 95


def test_add_grade_for_nonexistent_student():
    lecture = Lecture("Chemistry", "CHEM101")
    lecture.add_grade("Taivanbat", 90)
    assert "Taivanbat" not in lecture.students
