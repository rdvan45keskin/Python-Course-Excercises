# def cube():
#     for i in range(5):
#         yield i ** 3
# # iterator = iter(generator)
# for i in cube():
#     print(i)

# elemanı saklamaya gerek yoksa ve sadece ekranda görülmek isteniyosa bu daha mantıklı 
# bellek işgal edilmemiş olur

liste = [i**3 for i in range(5)]
print(liste)
generator = (i**3 for i in range(5))
for i in generator:
    print(i)


