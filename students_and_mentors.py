class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_skill(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git', 'Python']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

some_reviewer = Reviewer('John', 'Checker')
some_reviewer.courses_attached = ['Git']

some_lecturer = Lecturer('Rob', 'Tutor')
some_lecturer.courses_attached = ['Python']
best_student.lecturer_skill(some_lecturer, 'Python', 10)
print(some_lecturer.name, some_lecturer.surname)
print(some_lecturer.name, some_lecturer.surname, 'has grade: ', some_lecturer.grades)
print(some_lecturer.courses_attached)

print(some_reviewer.name, some_reviewer.surname)
print(some_reviewer.courses_attached)

print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)
