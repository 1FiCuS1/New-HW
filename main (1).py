class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.srgr = float()

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
        if not grade_counter:
            return 'нет оценок'
        else:
            for i in self.grades.values():
                for j in i:
                    grade_counter += j
            return float(grade_counter / len(self.grades))

    def __srt__(self):
        finished_courses = ', '.join(self.finished_courses)
        courses_in_progress = ', '.join(self.courses_in_progress)   

        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f' Средняя оценка за домашние задания: {self.srgr()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress}\n' \
              f'Завершенные курсы: {finished_courses}'      
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):
    def __init__(self, name, surname, grades):
        super().__init__(name, surname)
        self.grades = {}
        self.srgr = float()

    def srgr(self):
        grade_counter = 0
        if not grade_counter:
            return 'нет оценок'
        else:
            for i in self.grades.values():
                for j in i:
                    grade_counter += j
            return float(grade_counter / len(self.grades))  

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr()}'
        return res  

class  Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                 student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Ruoy', 'Eman',)
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ivan', 'Ivanov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Maria', 'Alekseeva')
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

def rating_lecture(list_lecture, course_name):
    summa = 0
    counter = 0
    for lektor in list_lecture:
        if lektor.courses_attached == [course_name]:
            for i in lektor.grades:
                summa += sum(lektor.grades[lektor])
                counter.extend(lektor)
            return float(sum(counter)/len(counter))
        
def rating_student(list_student, course_name):
    summa = 0
    counter = 0
    for student in list_student:
        if student.courses_in_progress == [course_name]:
            for i in student.grades:
                summa += sum(student.grades[student])
                counter.extend(student)
            return float(sum(counter)/len(counter))
        
print(f'Перечень студентов:\n {student_1}\n {student_2}\n {student_3}')
print()
print()
print()
print(f'Перечень лекторов:\n {best_lecture_1}\n {best_lecture_2}\n {best_lecture_3}')
print()
print()
print()
print(f'Результат сравнения студентов по средней оценке за домашние задания:\n {student_1.name} > {student_2.name} > {student_3.name}') 
print()
print()
print()
print(f'Результат сравнения лекторов по средней оценке за лекции:\n {best_lecture_1.name} > {best_lecture_2.name} > {best_lecture_3.name}')
print()
print()
print()
print(f'Средняя оценка за домашние задания по всем студентам: {student_1.srgr()}')
print()
print()
print()
print(f'Средняя оценка за лекции по всем лекторам: {best_lecture_1.srgr()}')       
    


        