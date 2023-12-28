class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
       

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and  course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка' 


    def srgr(self):
        grade_counter = 0
        if not self.grades:
            return 0,0
        list_ = []
        for i in self.grades.values():
            list_.extend(i)
        return sum(list_) / len(list_)

    def __str__(self):
        finished_courses = ', '.join(self.finished_courses)
        courses_in_progress = ', '.join(self.courses_in_progress)   

        return (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}\n' 
               f' Средняя оценка за домашние задания: {self.srgr()}\n' 
               f'Курсы в процессе обучения: {courses_in_progress}\n' 
               f'Завершенные курсы: {finished_courses}')

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() == other.srgr()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()
    
    def __lg__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() >= other.srgr()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def srgr(self):
        if not self.grades:
            return 0,0
        list_ = []
        for i in self.grades.values():
            list_.extend(i)
            return sum(list_)/len(list_)

    def __str__(self):
        return (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}\n' 
               f'Средняя оценка за лекции: {self.srgr()}')
    
    def __eq__(self, other):
        if not isinstance(other, Lecture):
            print('Такое сравнение некорректно')
            return
        return self.srgr() == other.srgr()

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()
    
    def __lg__(self, other):
        if not isinstance(other, Lecture):
            print('Такое сравнение некорректно')
            return
        return self.srgr() >= other.srgr()
        

class  Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                 student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
        


student_1 = Student('Ruoy', 'Eman', 'm')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ivan', 'Ivanov', 'm')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Maria', 'Alekseeva', 'f')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

best_lecture_1 = Lecture('Pavel', 'Pavlov')
best_lecture_1.courses_attached += ['Python']

best_lecture_2 = Lecture('Katrin', 'Ivanova')
best_lecture_2.courses_attached += ['Java']

best_lecture_3 = Lecture('Sergey', 'Sergeev')
best_lecture_3.courses_attached += ['Python']

nice_reviewer_1 = Reviewer('Some', 'Buddy')
nice_reviewer_1.courses_attached += ['Python']

nice_reviewer_2 = Reviewer('Sasha', 'Romanov')
nice_reviewer_2.courses_attached += ['Java']

nice_reviewer_3 = Reviewer('Max', 'Aleksandrenko')
nice_reviewer_3.courses_attached += ['Python']

student_1.rate_hw(best_lecture_1, 'Python', 10)
student_1.rate_hw(best_lecture_1, 'Python', 9)
student_1.rate_hw(best_lecture_3, 'Python', 8)

student_2.rate_hw(best_lecture_2, 'Java', 10)
student_2.rate_hw(best_lecture_1, 'Python', 9)
student_2.rate_hw(best_lecture_2, 'Java', 6)

student_3.rate_hw(best_lecture_3, 'Python', 10)
student_3.rate_hw(best_lecture_1, 'Python', 9)
student_3.rate_hw(best_lecture_2, 'Java', 8)

nice_reviewer_1.rate_hw(student_1, 'Python', 10)
nice_reviewer_1.rate_hw(student_2, 'Java', 9)
nice_reviewer_1.rate_hw(student_3, 'Python', 8)

nice_reviewer_2.rate_hw(student_1, 'Java', 10)
nice_reviewer_2.rate_hw(student_2, 'Java', 9)
nice_reviewer_2.rate_hw(student_3, 'Java', 8)

nice_reviewer_3.rate_hw(student_1, 'Python', 10)
nice_reviewer_3.rate_hw(student_2, 'Java', 9)
nice_reviewer_3.rate_hw(student_3, 'Python', 8)

list_student = [student_1, student_2, student_3]
list_lecture = [best_lecture_1, best_lecture_2, best_lecture_3]


def rating_student(list_student, course_name):
    all_grades = []
    for student in list_student:
        if (course_name in student.courses_in_progress and student.grades.get(course_name)):
            all_grades.append[course_name]

    return sum(all_grades) / len(all_grades) / len(list_student) if all_grades else 0.0

def rating_lecture(list_lecture, course_name):
    all_grades = []
    for lektor in list_lecture:
        if (course_name in lektor.courses_attached and lektor.grades.get(course_name)):
            all_grades.append[course_name]

    return sum(all_grades) / len(all_grades) / len(list_lecture) if all_grades else 0.0


def avg(grades: list) -> float:
    return sum(grades) / len(grades) if len(grades) > 0 else 0.0
def average_rating_course(peoples: list, course: str) -> float:
    list_grades = []
    for student in peoples:
        if tmp := student.grades.get(course):
            list_grades.append(avg(tmp))
    return avg(list_grades)       

def average_rating_course_lectors(peoples: list, course: str) -> float:
    list_grades = []
    for lektor in peoples:
        if tmp := lektor.grades.get(course):
            list_grades.append(avg(tmp))
    return avg(list_grades)


            
print(f'Перечень студентов:\n {student_1}\n\n {student_2}\n\n {student_3}')
print()
print()
print()
print(f'Перечень лекторов:\n {best_lecture_1}\n\n {best_lecture_2}\n\n {best_lecture_3}')
print()
print()
print()
print(f'Результат сравнения студентов по средней оценке за домашние задания:') 
print(max((student_1, student_2, student_3), key=lambda x: x.srgr()))
print()
print()
print(f'Результат сравнения лекторов по средней оценке за лекции:')
print(max((best_lecture_1, best_lecture_2, best_lecture_3), key=lambda x: x.srgr()))
print()
print()
print(f'Средняя оценка за домашние задания по всем студентам: {average_rating_course(peoples=[student_1, student_2, student_3], course="Python")}') 
print()
print()
print(f'Средняя оценка за лекции по всем лекторам: {average_rating_course_lectors(peoples=[best_lecture_1, best_lecture_2, best_lecture_3], course="Python")}') 
print()
