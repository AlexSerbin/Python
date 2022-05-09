class Student:

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def __repr__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Оценка: {self.grades}"


class Group:

    def __init__(self):
        self.student_list = []

    def plus_student(self, student):
        self.student_list.append(student)

    def __repr__(self):
        return str(self.student_list)


st = Student("Petya", "Pupkin", 4)
st2 = Student("Vasya", "Petkin", 4)
st3 = Student("Ktya", "Papine", 4)
st4 = Student("Dasha", "Pashina", 4)
print(st)

gr = Group()
gr.plus_student(st)
gr.plus_student(st2)
gr.plus_student(st3)
gr.plus_student(st4)

print(gr)



