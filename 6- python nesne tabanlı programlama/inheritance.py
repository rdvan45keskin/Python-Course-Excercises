# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), drink(), run()
# Student(Person),Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self ,fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person")
    
    def eat(self):
        print("Im eating")


class Student(Person):
    def __init__(self, fname, lname,number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student Created")
    #override = classın kendi içindeki method dışardan geleni ezer
    def who_am_i(self):
        print("Im a student")
    def sayHello(self):
        print("hello I am a Student")


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")





p1 = Person("Rıdvan","Keskin")
s1 = Student("Indigo","513",1256)
t1 = Teacher("Ehucu","Memduh","edebiyat")

print(p1.firstname+" "+p1.lastname)
print(s1.firstname+" "+s1.lastname+" "+str(s1.studentNumber))
print(t1.firstname+" "+t1.lastname+" "+t1.branch)
p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()
