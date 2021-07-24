# EP.4 OOP - CLASS
class Student:
    def __init__(self, name='John'):
        self.name = name
        self.point = 0
        self.lesson = 0

    def Hello(self):
        print(f'Hello World, i am {self.name}')

    def Coding(self):
        print('Coding')
        self.point += 5
        self.lesson += 1
    
    def ShowPoint(self):
        print(f'{self.name} has {self.point} point(s), learned {self.lesson}')

    def AddExtra(self, point):
        self.point += point

# CLASS INHERITANCE
class SpecialStudent(Student):
    def __init__(self, name='Jane', father='John'):
        super().__init__(name)
        self.father = father
        mafia = ['John Doe', 'Jane Doe']
        if father in mafia:
            self.point += 100
    
    # OVERIDE SUPER ATTRIBUTE
    def AddExtra(self, score):
        self.point += (score * 3)
        self.lesson += 1

class SpecialScore():
    def __init__(self):
        self.score = 500

st1 = Student('Jane')
st1.Hello()

st2 = Student()
st2.Hello()
st2.point += 5

print(st1.point)
print(st2.point)