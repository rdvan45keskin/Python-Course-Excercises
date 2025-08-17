# class
class Person:
    # class attributes == nitelikler   her zaman kullanılmayacak olan özellikler
    adress = "no information"
    # constructor(yapıcı method)
    def __init__(self, name, year):
        # object attributes            obje oluşturulurken mutlaka tanımlanmasını sağlar
        self.name = name
        self.birtyear = year
        print("init methodu çalıştı")
        # methods == methodlar

# object (instance)
p1 = Person(name = "Rıdvan",year = 2003)
p2 = Person("Indigo",2000)

# updating
p1.name = "ahmet"
p1.adress = "manisa"
# accessing object attributes
print(f"p1: name: {p1.name} year: {p1.birtyear} adress: {p1.adress}")
print(f"p2: name: {p2.name} year: {p2.birtyear} adress: {p2.adress}")

print(p1)
print(p2)