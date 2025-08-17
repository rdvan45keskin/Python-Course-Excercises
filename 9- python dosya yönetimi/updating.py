# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read(),end="")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")


# ****Sayfa sonunda güncelleme****
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nGüçsüz")


# ****Sayfa başında güncelleme****
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Hello World\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read(),end="")


# ****Sayfa ortasında güncelleme****
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(4,"Yaban\n")
    print(list)
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read(),end="")