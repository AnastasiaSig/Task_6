class Student:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def avg_rate(self):
        for course, grades in self.grades.items():
            self.mean = sum(grades) / len(grades)
            return self.mean

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.mean < other.mean
        return print('Нет такого студента!')

    def __str__(self):
        result = 'Имя: {}\nФамилия: {}\nКурсы в процессе изучения: {}, {}\nСредняя оценка за домашние задания: {:.1f}\nЗавершенные курсы: {}'.format(
            self.name, self.surname, *self.courses_in_progress, self.mean, *self.finished_courses)
        return result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.mean = 0

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)

    def rate_lect(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached and grade in range(1, 11):
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        for course, grades in self.grades.items():
            self.mean = sum(grades) / len(grades)
            return self.mean

    def __str__(self):
        result = 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции: {:.1f}'.format(self.name, self.surname, self.mean)
        return result

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.mean < other.mean
        return print('Нет такого лектора!')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)
print()

some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress.append('Python')
some_student.courses_in_progress.append('Git')
some_student.finished_courses.append('Введение в программирование')

some_reviewer.courses_attached.append('Python')
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_student.avg_rate()
print(some_student)
print()

some_student2 = Student('Ivan', 'Petrov')
some_student2.courses_in_progress.append('Python')
some_student2.courses_in_progress.append('Git')
some_student2.finished_courses.append('Введение в программирование')

some_reviewer.courses_attached.append('Python')
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 9)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_student2.avg_rate()
print(some_student2)
print()

print(some_student.__lt__(some_student2))
print()

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Git']
some_lecturer.rate_lect(some_student, 'Git', 10)
some_lecturer.rate_lect(some_student2, 'Git', 10)
some_lecturer.rate_lect(some_student, 'Git', 10)
some_lecturer.rate_lect(some_student2, 'Git', 10)
some_lecturer.rate_lect(some_student, 'Git', 10)
some_lecturer.rate_lect(some_student2, 'Git', 10)
some_lecturer.rate_lect(some_student, 'Git', 9)
some_lecturer.avg_rate()
print(some_lecturer)
print()

some_lecturer2 = Lecturer('Pavel', 'Ivanov')
some_lecturer2.courses_attached += ['Git']
some_lecturer2.rate_lect(some_student, 'Git', 8)
some_lecturer2.rate_lect(some_student2, 'Git', 10)
some_lecturer2.rate_lect(some_student, 'Git', 9)
some_lecturer2.rate_lect(some_student2, 'Git', 10)
some_lecturer2.rate_lect(some_student, 'Git', 9)
some_lecturer2.rate_lect(some_student2, 'Git', 10)
some_lecturer2.rate_lect(some_student, 'Git', 9)
some_lecturer2.avg_rate()
print(some_lecturer2)
print()

print(some_lecturer.__lt__(some_lecturer2))