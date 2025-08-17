from dbmanager import DbManager
import datetime
from Student import Student
# burada arayüz ve işlemler bulunuyor ve dbmanagerden sorguların sonuçlarını getiriyor
class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara göre dersler\n7-Çıkış için E basın"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "E":
                break
            elif islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            else:
                print("geçersiz işlem")

    def addStudent(self):
        self.displayClasses()
        classid = int(input("hangi sınıf: "))
        number = input("numara: ")
        name = input("ad: ")
        surname = input("soyad: ")
        # year = int(input("yıl: "))
        # month = int(input("ay: "))
        # day = int(input("gün: "))
        # birthday = datetime.date(year,month,day)
        birthday = input("tarih girin (YYYY-MM-DD): ")
        gender = input("cinsiyet (E/K): ")

        student = Student(None,number,name,surname,birthday,gender,classid)
        self.db.addorEditStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id:"))

        student = self.db.getStudentById(studentid)

        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].geneder = input("cinsiyet (E/K): ") or student[0].gender
        student[0].classid = input("sınıf: " ) or student[0].classid
        student[0].birthday = input("birthday (YYYY-MM-DD): ") or student[0].birthday
        self.db.addorEditStudent(student[0])

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id:"))

        self.db.deleteStudent(studentid)

    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")

    def displayStudents(self):
        self.displayClasses()
        classid = int(input("hangi sınıf: "))

        students = self.db.getStudentsByClassId(classid)
        print("öğrenci listesi")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
        
        return classid








app = App()
app.initApp()