x,y,z = 2,6,10
numbers = 1,5,7,10,6
inputs = []
# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# for i in range(2):
#     a=int(input(f"{i+1}. sayıyı girin: "))
#     inputs.append(a)
# result=(inputs[0]*inputs[1])-(x+y+z)
# print(result)

# 2- y nin x e kalansız bölümünü hesaplayın
result2 = y//x
print(result2)

# 3- (x,y,z) toplamının mod 3 ü nedir
result3 = (x+y+z)%3
print(result3)

# 4- y nin x. kuvvetini hesaplayın
result4 = y**x
print(result4)

# 5- x,*y,z = numbers işlemine göre z nin küpü kaçtır
x,*y,z = numbers
result5 = z**3
print(result5)

# 6- x,*y,z = numbers işlemine göre y nin küpü kaçtır
result6 = y**3
print(result6)