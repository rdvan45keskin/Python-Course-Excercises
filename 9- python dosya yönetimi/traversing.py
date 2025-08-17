with open("newfile2.txt","r",encoding="utf-8") as file:
    content =  file.read(10)
    print(content)
    file.seek(0)        #cursorun nereye gideceğini kontrol eder
    print(file.tell())  #cursorun konumunu verir
    content2 = file.read(10)
    print(content2)


