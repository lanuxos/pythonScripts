class Player:
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.number = ''

class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

class Players:
    pass

def PlayerInit():
    p3 = Players()
    p3.fullname = "Lanuxos"
    print(p3.fullname)

# PlayerInit()

class Person:
    def __init__(self, fname=None, lname=None, country="Laos"):
        self.fname = fname
        self.lname = lname
        self.country = country

if __name__ == '__main__':
    p1 = Player()
    p1.fname = 'Loris'
    p1.lname = 'Karius'
    p1.number = '10'
    # print(p1.fname, p1.lname, p1.number)

    p2 = Player2('La', "nuxos", 17)
    # print(p2.fname, p2.lname, p2.number)

    p3 = Person()
    print(p3.country)

    p4 = Person('La', 'NuxOS', 'Laos')
    print(p4.fname)
    print(p4.lname)
    print(p4.country)
