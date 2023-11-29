class Student:

  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def lecturer_skill(self, lecturer, course, grade):
    if isinstance(
        lecturer, Lecturer
    ) and course in lecturer.courses_attached and course in self.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    student_grades = list(self.grades.values())
    grade_sum = 0
    count_ = 0
    for course in student_grades:
      for grade in course:
        grade_sum += grade
        count_ += 1
    student_avg_grade = grade_sum / count_
    return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade: {student_avg_grade} \nCourses in progress{self.courses_in_progress} \nCourses finished: {self.finished_courses}'

  def students_compare(self, student):
    if isinstance(student, Student):
      first_grades = list(self.grades.values())
      second_grades = list(student.grades.values())
      grades_1 = []
      grades_2 = []
      for grade, mark in first_grades, second_grades:
        grades_1 += grade
        grades_2 += mark
      if (sum(grades_1) / len(grades_1)) > (sum(grades_2) / len(grades_2)):
        return print(
            f'{self.name} {self.surname} круче {student.name} {student.surname}'
        )
      elif (sum(grades_1) / len(grades_1)) < (sum(grades_2) / len(grades_2)):
        return print(
            f'{student.name} {student.surname} круче {self.name} {self.surname}'
        )
      else:
        return print('Оба молодцы')
    else:
      return print('Ошибка')


class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []


class Reviewer(Mentor):

  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.courses_attached = []

  def __str__(self):
    return f'Name: {self.name} \nSurname: {self.surname}'

  def rate_hw(self, student, course, grade):
    if isinstance(
        student, Student
    ) and course in self.courses_attached and course in student.courses_in_progress:
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

  def __str__(self):
    grades_list = (self.grades)['Python']
    grade_sum = 0
    for grade in grades_list:
      grade_sum += grade
    lecturer_avg_grade = grade_sum / len(grades_list)
    return f'Name: {self.name} \nSurname: {self.surname} \nAverage grade: {lecturer_avg_grade}'

  def lecturers_compare(self, lecturer):
    if isinstance(lecturer, Lecturer):
      first_grades = list(self.grades.values())
      second_grades = list(lecturer.grades.values())
      grades_1 = []
      grades_2 = []
      for grade, mark in zip(first_grades, second_grades):
        grades_1 += grade
        grades_2 += mark
      if (sum(grades_1) / len(grades_1)) > (sum(grades_2) / len(grades_2)):
        return print(
            f'{self.name} {self.surname} круче {lecturer.name} {lecturer.surname}'
        )
      elif (sum(grades_1) / len(grades_1)) < (sum(grades_2) / len(grades_2)):
        return print(
            f'{lecturer.name} {lecturer.surname} круче {self.name} {self.surname}'
        )
      else:
        return print('Оба молодцы')
    else:
      return print('Ошибка')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git', 'Python']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 8, 10, 6, 10]
best_student.grades['Python'] = [10, 7]

worst_student = Student('Bob', 'Dilan', 'your_gender')
worst_student.finished_courses += ['Git', 'Python']
worst_student.courses_in_progress += ['Python']
worst_student.grades['Git'] = [7, 3, 4, 5, 10]
worst_student.grades['Python'] = [4, 6]

some_reviewer = Reviewer('John', 'Checker')
some_reviewer.courses_attached = ['Git']

some_lecturer = Lecturer('Rob', 'Tutor')
some_lecturer.courses_attached = ['Python']
best_student.lecturer_skill(some_lecturer, 'Python', 10)
best_student.lecturer_skill(some_lecturer, 'Python', 7)

other_lecturer = Lecturer('Mike', 'Mickey')
other_lecturer.courses_attached = ['Python']
best_student.lecturer_skill(other_lecturer, 'Python', 9)
best_student.lecturer_skill(other_lecturer, 'Python', 3)

#print(some_lecturer.name, some_lecturer.surname)
#print(some_lecturer.name, some_lecturer.surname, 'has grades: ', some_lecturer.grades)
#print(some_lecturer.courses_attached)

# print(other_lecturer.name, other_lecturer.surname)
# print(other_lecturer.name, other_lecturer.surname, 'has grades: ',
#       other_lecturer.grades)
# print(other_lecturer.courses_attached)

# print(some_reviewer.name, some_reviewer.surname)
# print(some_reviewer.courses_attached)
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)
#
# print(some_reviewer)
print(other_lecturer.grades)
print(some_lecturer)

print(other_lecturer)

print(best_student)

print(worst_student)

best_student.students_compare(worst_student)

some_lecturer.lecturers_compare(other_lecturer)

