class Player:
    # attributes
    eyes = 'Blue'
    age = 22
    # method
    def firstMethod(self):
        print('This is the first method of Player class')


obj = Player()
obj.firstMethod()
print('EYE: {} AGE:{}'.format(obj.eyes, obj.age))

print('---self---')

class SelfPlayer:
    def createName(self, name):
        self.name = name
    def displayName(self):
        print("Hello %s" % self.name)
        
obj1 = SelfPlayer()
obj1.createName('LA')
obj1.displayName()

print('---super & sub class---')

class Dad:
    name = 'papa'
    
    def SayHi(self):
        print('Hi dad')
    def Greeting(self, name):
        print(f'Hello {name}')

class ChildClass(Dad):
    def Goodbye(self):
        print('Goodbye')
obj2 = ChildClass()
obj2.SayHi()
obj2.Greeting('Child')
obj2.Goodbye()
print(obj2.name)

print('---multi-parent class---')

class Mom:
    def Order(self):
        print('Stop!')
class Children(Dad, Mom):
    def Answer(self):
        print('Ok sir')

obj3 = Children()
obj3.SayHi()
obj3.Order()
obj3.Answer()

print('------')