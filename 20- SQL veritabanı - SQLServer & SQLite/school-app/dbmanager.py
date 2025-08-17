import pydoc
from datetime import datetime
from connection_S import conn,cursor
from Student import Student
from Teacher import Teacher
from Class import Class



# dbmanagerde sql sorguları çalıştırılıyor

class DbManager:
    def __init__(self):
        self.connection = conn
        self.cursor = cursor

    def getStudentById(self,id):
        sql = "select * from Students Where ID = ?"
        value = (id,)
        try:
            self.cursor.execute(sql,value)
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
            # print(type(obj))
            # return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except Exception as ex:
            print("hata:" ,ex)

    def getClasses(self):
        sql = "select * from class"
        try:
            self.cursor.execute(sql)
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except Exception as ex:
            print("hata:" ,ex)

    def getStudentsByClassId(self,classid):
        sql = "select * from Students Where ClassId = ?"
        value = (classid,)
        try:
            self.cursor.execute(sql,value)
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except Exception as ex:
            print("hata:" ,ex)

    def addorEditStudent(self, student: Student):
        if student.id==0:
            sql = "INSERT INTO Students(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (?,?,?,?,?,?)"
            value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
            message = "eklendi"
        elif student.id>0:
            sql = "Update Students Set StudentNumber=?, Name=?, Surname=?,Birthdate=?,gender=?,ClassId=? where ID= ?"
            value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
            message = "güncellendi"
        
        try:
            self.cursor.execute(sql,value)
            self.connection.commit()
            self.cursor.execute("SELECT @@ROWCOUNT")
            rowcount = self.cursor.fetchone()[0]
            print(f"{rowcount} tane kayıt {message}")
        except Exception as e:
            print("hata",e)
    """
    def addStudent(self, student: Student):
        sql = "INSERT INTO Students(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (?,?,?,?,?,?)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)

        try:
            self.cursor.execute(sql,value)
            self.connection.commit()
            self.cursor.execute("SELECT @@ROWCOUNT")
            rowcount = self.cursor.fetchone()[0]
            print(f"{rowcount} tane kayıt eklendi")
        except Exception as e:
            print("hata",e)

    def editStudent(self, student: Student):
        sql = "Update Students Set StudentNumber=?, Name=?, Surname=?,Birthdate=?,gender=?,ClassId=? where ID= ?"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)

        try:
            self.cursor.execute(sql,value)
            self.connection.commit()
            self.cursor.execute("SELECT @@ROWCOUNT")
            rowcount = self.cursor.fetchone()[0]
            print(f"{rowcount} tane kayıt güncellendi")
        except Exception as e:
            print("hata",e)
    """
    def deleteStudent(self,studentid):
        sql = "delete from students where ID=?"
        value = (studentid,)
        try:
            self.cursor.execute(sql,value)
            self.connection.commit()
            self.cursor.execute("SELECT @@ROWCOUNT")
            rowcount = self.cursor.fetchone()[0]
            print(f"{rowcount} tane kayıt silindi")
        except Exception as e:
            print("hata",e)        

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass



db = DbManager()
# student = db.getStudentById(8)

# std = Student(None,513,"Rıdvan","Keskin","2003-06-19","E",3)
# db.addStudent(std)

# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(3)
# print(students[0].name)
# print(students[3].name)

# std = Student(None,134,"Gülcan","Keskin","2007-03-19","K",3)
# db.addorEditStudent(std)
# student = db.getStudentById(8)
# student[0].name = "Cınar"
# db.addorEditStudent(student[0])

