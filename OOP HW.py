class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    # Оценка лекторов
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    # Средняя оценка за домашние задания 
    def rating(self):
        s, l = 0, 0
        for course in self.grades.values():
            s += sum(course)
            l += len(course)
        average_rating = s / l
        return average_rating        

    # Магический метод
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.rating()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    # Сравнение по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student!")
            return
        return self.rating() < other.rating()   

    # Средняя оценка за домашние задания по всем студентам в рамках конкретного курса
    def rating_course(self, course):
        s, l = 0, 0
        for _ in self.grades.keys():
            if _ == course:
                s += sum(self.grades[course])
                l += len(self.grades[course])
        average_rating = s / l
        return average_rating    

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}

    # Средняя оценка за лекции
    def rating(self):
        s, l = 0, 0
        for course in self.grades.values():
            s += sum(course)
            l += len(course)
        average_rating = s / l
        return average_rating  

    # Магический метод
    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rating()}"
        return res
    
    # Сравнение по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer!")
            return
        return self.rating() < other.rating()

    # Средняя оценка за лекции всех лекторов в рамках курса
    def rating_course(self, course):
        s, l = 0, 0
        for _ in self.grades.keys():
            if _ == course:
                s += sum(self.grades[course])
                l += len(self.grades[course])
        average_rating = s / l
        return average_rating  


class Reviewer(Mentor):
    # Выставление студентам оценки за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Магический метод
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

# Полевые испытания:
# Студенты
student_1 = Student("Иван", "Иванов", "М")
student_1.finished_courses = ["Введение в программирование"]
student_1.courses_in_progress = ["Python"]
student_1.grades = {}

student_2 = Student("Иванка", "Иванова", "Ж")
student_2.finished_courses = ["Введение в программирование"]
student_2.courses_in_progress = ["Python"]
student_2.grades = {}

# Лекторы
lecturer_1 = Lecturer("Жорж", "Милославский")
lecturer_1.courses_attached += ["Python"]
lecturer_2 = Lecturer("Венера", "Милосская")
lecturer_2.courses_attached += ["Python"]

# Проверяющие
reviewer_1 = Reviewer("Арнольд", "Столоне")
reviewer_1.courses_attached += ["Python"]
reviewer_2 = Reviewer("Жасмин", "Фиолетова")
reviewer_2.courses_attached += ["Python"]

# Оценки студентам
reviewer_1.rate_hw(student_1, "Python", 8)
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Python", 7)

reviewer_2.rate_hw(student_2, "Python", 8)
reviewer_2.rate_hw(student_2, "Python", 9)
reviewer_2.rate_hw(student_2, "Python", 10)

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, "Python", 9)
student_1.rate_lecturer(lecturer_1, "Python", 10)
student_1.rate_lecturer(lecturer_1, "Python", 9)

student_1.rate_lecturer(lecturer_2, "Python", 10)
student_1.rate_lecturer(lecturer_2, "Python", 9)
student_1.rate_lecturer(lecturer_2, "Python", 10)

# Списки
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def rating_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for student in student_list:
        for course in student.grades:
            student_sum_rating = student.rating_course(course)
            sum_rating += student_sum_rating
            quantity_rating += 1
    average_rating = sum_rating / quantity_rating
    return average_rating

print(student_1)
print("----------------------")
print(student_2)
print("----------------------")
print(lecturer_1)
print("----------------------")
print(lecturer_2)
print("----------------------")
print(reviewer_1)
print("----------------------")
print(reviewer_2)
print("----------------------")
print(rating_course("Python", student_list))
print("----------------------")
print(rating_course("Python", lecturer_list))