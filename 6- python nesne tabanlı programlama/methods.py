# # class
# class Person:
#     # class attributes == nitelikler   her zaman kullanılmayacak olan özellikler
#     adress = "no information"
#     # constructor(yapıcı method)
#     def __init__(self, name, year):
#         # object attributes            obje oluşturulurken mutlaka tanımlanmasını sağlar
#         self.name = name
#         self.birtyear = year
#         print("init methodu çalıştı")
    
#     # instance methods                  objelere hizmet eder
#     def intro(self):
#         print("hello there. I am "+self.name)
#     # instance methods 
#     def calculateAge(self):
#         return 2024 - self.birtyear





# # object (instance)
# p1 = Person(name = "Rıdvan",year = 2003)
# p2 = Person("Indigo",2000)
# p1.intro()
# p2.intro()
# print(f"Adım: {p1.name} yaşım: {p1.calculateAge()}")
# print(f"Adım: {p2.name} yaşım: {p2.calculateAge()}")


class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self ,yaricap = 1):
        self.yariCap = yaricap
    #methods
    def cevreHesapla(self):
        return 2*self.pi*self.yariCap
    
    def alanHesapla(self):
        return self.pi * (self.yariCap**2)
    
c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1 => alan = {c1.alanHesapla()} cevre = {c1.cevreHesapla():1.4}")
print(f"c2 => alan = {c2.alanHesapla()} cevre = {c2.cevreHesapla():1.4}")