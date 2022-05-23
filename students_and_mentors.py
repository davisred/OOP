class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rate_student()}\n'
                f'Курсы в прогрессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def __eq__(self, other):
        return self.average_rate_student() == self.average_rate_student()

    def __lt__(self, other):
        return self.average_rate_student() < self.average_rate_student()

    def __gt__(self, other):
        return self.average_rate_student() > self.average_rate_student()

    def average_rate_student(self):
        rate_list = []
        for v in self.grades.values():
            rate_list += v
        if len(rate_list) >= 2:
            average = sum(rate_list) / len(rate_list)
            return average
        else:
            raise Exception('Недостаточно оценок для расчета среднего балла')

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.rating_lections:
                lecturer.rating_lections[course] += [grade]
            else:
                lecturer.rating_lections[course] = [grade]
        else:
            raise Exception("Ошибка")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.rating_lections = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_rate_lecturer()}\n')

    def __eq__(self, other):
        return self.average_rate_lecturer() == self.average_rate_lecturer()

    def __lt__(self, other):
        return self.average_rate_lecturer() < self.average_rate_lecturer()

    def __gt__(self, other):
        return self.average_rate_lecturer() > self.average_rate_lecturer()

    def average_rate_lecturer(self):
        rate_list = []
        for v in self.rating_lections.values():
            rate_list += v
        if len(rate_list) >= 2:
            average = sum(rate_list) / len(rate_list)
            return average
        else:
            raise 'Недостаточно оценок для расчета среднего балла'


class Reviewer(Mentor):
    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}\n')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise Exception('Ошибка')


def show_rate_of_course(student_list, course):
    all_grades = []
    for student in student_list:
        for k, v in student.grades.items():
            if k == course:
                all_grades += v
    return f'Средняя оценка домашних работ по курсу {course}: ' \
           f'{sum(all_grades) / len(all_grades)}'


def show_rate_of_lections(lectors, course):
    all_grades = []
    for lecturer in lectors:
        for k, v in lecturer.rating_lections.items():
            if k == course:
                all_grades += v
    return f'Средняя оценка лекций по курсу {course}: ' \
           f'{sum(all_grades) / len(all_grades)}'


lecturer_1 = Lecturer('Diane', 'Choksondik')
lecturer_1.courses_attached += ['Python', 'Django', 'JavaScript']
lecturer_2 = Lecturer('Herbert', 'Garrison')
lecturer_2.courses_attached += ['Python', 'Django', 'JavaScript']
lecturers = [lecturer_1, lecturer_2]

student_1 = Student('Eric', 'Cartman', 'male')
student_1.courses_in_progress += ['Django', 'JavaScript']
student_1.finished_courses += ['Python']
student_1.rate_lection(lecturer_1, 'Python', 4)
student_1.rate_lection(lecturer_2, 'Python', 6)

student_2 = Student('Kenny', 'MacCormick', 'male')
student_2.courses_in_progress += ['Django', 'JavaScript']
student_2.finished_courses += ['Python']
student_2.rate_lection(lecturer_1, 'Python', 6)
student_2.rate_lection(lecturer_2, 'Python', 8)
students = [student_1, student_2]

reviewer_1 = Reviewer('Richard', 'Adler')
reviewer_1.courses_attached += ['Django', 'Python', 'JavaScript']
reviewer_1.rate_hw(student_1, 'Django', 5)
reviewer_1.rate_hw(student_1, 'Django', 8)
reviewer_1.rate_hw(student_1, 'JavaScript', 4)
reviewer_1.rate_hw(student_1, 'JavaScript', 10)

reviewer_2 = Reviewer('Mister', 'Mackey')
reviewer_2.courses_attached += ['Django', 'Python', 'JavaScript']
reviewer_2.rate_hw(student_2, 'Django', 6)
reviewer_2.rate_hw(student_2, 'Django', 9)
reviewer_2.rate_hw(student_2, 'JavaScript', 7)
reviewer_2.rate_hw(student_2, 'JavaScript', 9)

print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(Student.average_rate_student(student_1) == Student.average_rate_student(student_2))
print(Student.average_rate_student(student_1) > Student.average_rate_student(student_2))
print(Student.average_rate_student(student_1) < Student.average_rate_student(student_2))
print(Lecturer.average_rate_lecturer(lecturer_1) == Lecturer.average_rate_lecturer(lecturer_2))
print(Lecturer.average_rate_lecturer(lecturer_1) > Lecturer.average_rate_lecturer(lecturer_2))
print(Lecturer.average_rate_lecturer(lecturer_1) < Lecturer.average_rate_lecturer(lecturer_2))
print(show_rate_of_course(students, 'JavaScript'))
print(show_rate_of_lections(lecturers, 'Python'))
