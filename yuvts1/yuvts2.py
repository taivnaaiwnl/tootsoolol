class Lecture:
    def __init__(self, lecture_name, lecture_index):
        self.lecture_name = lecture_name
        self.lecture_index = lecture_index
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = None

    def add_grade(self, student_name, grade):
        if student_name in self.students:
            self.students[student_name] = grade
        else:
            print(f"{student_name} suragch oldsongui.")

    def get_total_students(self):
        return len(self.students)

    def get_all_students_total_average(self):
        if not self.students:
            return 0
        total_grade = sum(
            grade for grade in self.students.values() if grade is not None
        )
        total_students_with_grades = sum(
            1 for grade in self.students.values() if grade is not None
        )
        return (
            total_grade / total_students_with_grades
            if total_students_with_grades
            else 0
        )
