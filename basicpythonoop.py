# Basic Python OOP

class Student:
    
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.exp = 0
        self.lesson = 0
        self.vehicle = 'Bus'

    @property
    def Fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    def Coding(self):
        self.AddExp()
        print('{} Learning to code ...'.format(self.Fullname))

    def ShowExp(self):
        print('{} now have {} point(s), {} time(s)'.format(self.Fullname, self.exp, self.lesson))

    def AddExp(self):
        self.exp += 10
        self.lesson += 1

    def __str__(self):
        return self.Fullname

    def __repr__(self):
        return self.Fullname

    def __add__(self, other):
        return self.exp + other.exp

class Tesla:
    def __init__(self):
        self.model = 'Model S'

    def SelfDriving(self):
        print('is auto pilot vehicle')

    def __str__(self):
        return self.model

class SpecialStudent(Student):

    def __init__(self, name, lastname, father):
        super().__init__(name, lastname)
        self.father = father
        self.vehicle = Tesla()
        print('My name is {}, A Special Student, the son of {}'.format(self.Fullname, self.father))

    def AddExp(self):
        self.exp += 30
        self.lesson += 2

class Teacher:
    
    def __init__(self, fullname):
        self.fullname = fullname
        self.students = []

    def CheckStudent(self):
        for i, st in enumerate(self.students):
            print('{} has {} student(s): '.format(self.fullname, len(self.students)))
            print('{}./ {} [{}], attend {} class(es)'.format(i+1, st.Fullname, st.exp, st.lesson))
            
    def AddStudent(self, st):
        self.students.append(st)
    
if __name__ == '__main__':
    allStudents = []

    tc1 = Teacher('LANUXOS')
    tc2 = Teacher('LATOUY')

    st1 = Student('La', 'Touy')
    tc1.AddStudent(st1)
    allStudents.append(st1)
    print('FULLNAME:', st1.Fullname)
    for i in range(3):
        st1.Coding()
    st1.ShowExp()
    print('Vehicle', st1.vehicle)
    print(isinstance(st1, SpecialStudent))

    print('****************')

    st2 = SpecialStudent('Nilavath', "Taybanvilay", 'Mr')
    tc2.AddStudent(st2)
    allStudents.append(st2)
    print('FULLNAME:', st2.Fullname)
    st2.Coding()
    st2.ShowExp()
    print('Vehicle', st2.vehicle)
    if isinstance(st2.vehicle, Tesla):
        st2.vehicle.SelfDriving()
    print(isinstance(st2, SpecialStudent))

    print('Students', allStudents)

    print('****************')

    tc1.CheckStudent()
    tc2.CheckStudent()

    print('****************')

    print('__add__:', st1 + st2)