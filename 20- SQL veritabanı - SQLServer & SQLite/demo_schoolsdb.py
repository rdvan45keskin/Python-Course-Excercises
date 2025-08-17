# 1- schooldb isminde bir database oluşturup students tablosu oluşturun
#     # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısı oluşturun

# 3- Aşağıdaki bilgiler için insert sorguları oluşturun
#     ("101","Ahmet","Yılmaz",datetime.datetime(2005, 5, 17),"E"),
#     ("102","Ali","Can",datetime.datetime(2005, 6, 17),"E"),
#     ("103","Canan","Tan",datetime.datetime(2005, 7, 7),"K"),
#     ("104","Ayşe","Taner",datetime.datetime(2005, 9, 23),"K"),
#     ("105","Bahaadır","Toksöz",datetime.datetime(2004, 7, 27),"E"),
#     ("106","Ali","Cenk",datetime.datetime(2003, 8, 25),"E"),

# 4- Aşağıdaki sorguları yazınız.
#     a- Tüm öğrenci kayıtlarını alınız
#     b- tüm öğrencilerin sadece öğrenci no, ad ve soyadlarını alın
#     c- sadece kız öğrencilerin ad ve soyadlarını alın
#     d- 2003 doğumlu öğrenci bilgilerini alın
#     e- ismi ali ve doğum tarihi 2005 olan öğrencileri alın
#     f- ad ya da soyadı içinde "an" ifadesi geçen kayıtları alın
#     g- kaç erkek öğrenci vardır
#     h- kız öğrencileri harf sırasına göre getiriniz

# 5- Aşağıdaki güncelleme sorularını yapınız.
#     a- id' e göre aldığınız bir öğrencinin bilgilerini değiştirin
#     b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini değiştirin

from datetime import datetime
from connection import conn

class Student:
    connection = conn
    mycursor = conn.cursor()
    def __init__(self, id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Students(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (?,?,?,?,?)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        

        try:
            Student.mycursor.execute(sql,value)
            Student.connection.commit()
            Student.mycursor.execute("SELECT @@ROWCOUNT")
            rowcount = Student.mycursor.fetchone()[0]
            print(f"{rowcount} tane kayıt eklendi")
        except Exception as e:
            print("hata",e)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(List):
        sql = "INSERT INTO Students(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (?,?,?,?,?)"
        values = List
        
        try:
            Student.mycursor.executemany(sql,values)
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount+1+len(ogrenciler)} tane kayıt eklendi")
        except Exception as e:
            print("hata",e)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        sql = "select * from Students"
        sql = "select StudentNumber,Name,Surname from Students"
        sql = "select Name,Surname from Students where gender='K'"
        sql = "select * from Students where YEAR(Birthdate)=2003"
        sql = "select * from Students where name='Ali' and YEAR(Birthdate)=2005"
        sql = "select * from Students where name like '%an%' or surname like '%an%'"
        sql = "select Count(ID) from Students where gender='E'"
        sql = "select * from Students where gender='K' order by name,surname,StudentNumber"
        sql = "select top 5 * from Students"


        try:
            Student.mycursor.execute(sql)
            result = Student.mycursor.fetchall()      # for döngüsü oluşturulur
            # result = Student.mycursor.fetchone()    # for döngüsü oluşturulamaz tek bir bilgiyi seçer
            for i in result:
                print(i)
                # print(f"ID: {i[0]} Number: {i[1]} name: {i[2]} Surname: {i[3]} Birthdate: {i[4]} Gender: {i[5]}")
                # print(f"name: {i[0]} price: {i[1]}")
        except Exception as ex:
            print("hata: ",ex)
        finally:
            conn.close()
            print("bağlantı kapandı")

    @staticmethod
    def getStudentByID(id):
        sql = "select * from students where ID=?"
        values = (id)

        try:
            Student.mycursor.execute(sql,values)
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except Exception as ex:
            print("hata: ",ex)

    def StudentUpdate(self):
        sql = "Update Students Set StudentNumber=?, Name=?, Surname=?,Birthdate=?,gender=? where ID= ?"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)

        try:
            Student.mycursor.execute(sql,values)
            conn.commit()
            Student.mycursor.execute("SELECT @@ROWCOUNT")
            rowcount = Student.mycursor.fetchone()[0]
            print(f"{rowcount} tane kayıt güncellendi")
        except Exception as ex:
            print("hata: ",ex)


    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from students where gender=?"
        values = (gender,)

        try:
            Student.mycursor.execute(sql,values)
            return Student.mycursor.fetchall()
        except Exception as ex:
            print("hata: ",ex)

    @staticmethod
    def StudentsUpdate(liste):
        sql = "Update Students Set StudentNumber=?, Name=?, Surname=?,Birthdate=?,gender=? where ID= ?"
        values = []
        order = [1,2,3,4,5,0]

        # bir diziyi belli bir diziye göre sıralama
        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        try:
            Student.mycursor.executemany(sql,values)
            conn.commit()
            print(f"{Student.mycursor.rowcount+1+len(liste)} tane kayıt güncellendi")
        except Exception as ex:
            print("hata: ",ex)


# 5- Aşağıdaki güncelleme sorularını yapınız.
#     a- id' e göre aldığınız bir öğrencinin bilgilerini değiştirin
#     b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini değiştirin


# selin = Student("130", 'Selin', 'Demir', datetime(2003,11,25), 'K')
# selin.saveStudent()


# mycursor.execute("CREATE DATABASE schooldb")
# mycursor.execute("""
# CREATE TABLE Students(
# ID smallint primary key Identity(1,1),
# StudentNumber smallint not null UNIQUE,
# Name Varchar(25) not null,
# Surname varchar(25) not null,
# Birthdate datetime not null,
# Gender char(1) not null
# )
# """)

# list = []


ogrenciler = [
    ("601","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("602","Ali","Can",datetime(2005, 6, 17),"E"),
    ("603","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("604","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("605","Bahaadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("606","Ali","Cenk",datetime(2003, 8, 25),"E"),
]

# Student.saveStudents(ogrenciler)
# Student.StudentInfo()

# Güncelleme

# while True:
#     ID = input("Güncellenecek ID bilgisini yazın")
#     student = Student.getStudentByID(ID)
#     name = input("Yeni Adı giriniz: ")
#     student.name = name
#     surname = input("Yeni Soyadı girin: ")
#     student.surname = surname
#     student.StudentUpdate()

#     choose = print("Başka işlem yapmak ister misiniz(y/n): ")
#     if choose == "y":
#         pass
#     else:
#         break

students = Student.getStudentsGender("E")

liste = []
for std in students:
    std = list(std)
    std[2] = "Mr. " + std[2]
    liste.append(std)

Student.StudentsUpdate(liste)











