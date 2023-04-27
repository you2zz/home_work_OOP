class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'    
    
    def __average_grade(self, grades):
        all_grades = []
        for _, g in grades.items():
            all_grades += g
        average_grade= sum(all_grades) / len(all_grades) 
        return round(average_grade, 1)
    
    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade(self.grades)}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'  
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнивать студентов с преподавателями!')
            return
        return self.__average_grade(self.grades) < other.__average_grade(other.grades)
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def __average_grade(self, grades):
        all_grades = []
        for _, g in grades.items():
            all_grades += g
        average_grade= sum(all_grades) / len(all_grades) 
        return round(average_grade, 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade(self.grades)}'  
        return res  
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нельзя сравнивать преподавателей со студентами!'
        return self.__average_grade(self.grades) < other.__average_grade(other.grades)

class Reviewer(Mentor):
        
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

# Экземпляры классa Student:

ivan_student = Student('Иван', 'Царевич', 'мужской')
ivan_student.courses_in_progress += ['ООП и работа с API', 'Git - система контроля версий']
ivan_student.finished_courses += ['Основы языка программирования Python']

helen_student = Student('Елена', 'Прекрасная', 'женский')
helen_student.courses_in_progress += ['ООП и работа с API', 'Git - система контроля версий']
helen_student.finished_courses += ['Основы языка программирования Python']

# Экземпляры классa Lecturer:

bayan_lecturer = Lecturer('Кот', 'Баян')
bayan_lecturer.courses_attached += ['ООП и работа с API']

sirena_lecturer = Lecturer('Сирена', 'Морская')
sirena_lecturer.courses_attached += ['Git - система контроля версий']

# Экземпляры классa Reviewer:

dobrinya_reviewer = Reviewer('Добрыня', 'Никитич')
dobrinya_reviewer.courses_attached += ['ООП и работа с API']

popovich_reviewer = Reviewer('Алеша', 'Попович')
popovich_reviewer.courses_attached += ['Git - система контроля версий']

# Студенты накидывают оценки лекторам:

ivan_student.rate_hw(bayan_lecturer, 'ООП и работа с API', 10)
ivan_student.rate_hw(bayan_lecturer, 'ООП и работа с API', 9)
ivan_student.rate_hw(sirena_lecturer, 'Git - система контроля версий', 9)
ivan_student.rate_hw(sirena_lecturer, 'Git - система контроля версий', 8)

helen_student.rate_hw(bayan_lecturer, 'ООП и работа с API', 9)
helen_student.rate_hw(bayan_lecturer, 'ООП и работа с API', 9)
helen_student.rate_hw(sirena_lecturer, 'Git - система контроля версий', 9)
helen_student.rate_hw(sirena_lecturer, 'Git - система контроля версий', 7)
 
# Ревьюверы оценивают студентов:

dobrinya_reviewer.rate_hw(ivan_student, 'ООП и работа с API', 8)
dobrinya_reviewer.rate_hw(ivan_student, 'ООП и работа с API', 9)
dobrinya_reviewer.rate_hw(helen_student, 'ООП и работа с API', 10)
dobrinya_reviewer.rate_hw(helen_student, 'ООП и работа с API', 10)

popovich_reviewer.rate_hw(ivan_student, 'Git - система контроля версий', 7)
popovich_reviewer.rate_hw(ivan_student, 'Git - система контроля версий', 8)
popovich_reviewer.rate_hw(helen_student, 'Git - система контроля версий', 10)
popovich_reviewer.rate_hw(helen_student, 'Git - система контроля версий', 9)

# Выводим информацию о студентах:
print(ivan_student)
print()
print(helen_student)
print()
print(ivan_student > helen_student, ivan_student < helen_student)
print()

# Выводим информацию о лекторах:
print(bayan_lecturer)
print()
print(sirena_lecturer)
print()
print(sirena_lecturer < bayan_lecturer, sirena_lecturer > bayan_lecturer)
print()