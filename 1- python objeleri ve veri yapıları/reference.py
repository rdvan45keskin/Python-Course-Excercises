# value types => string, number   

# farklı adreste oldukları için birinin değişmesi diğerini etkilemez
x = 5
y = 25

x = y

y = 10

print(x,y)

# reference types => list

# eşitlendikten sonra aynı adrese kondukları için birinin değişmedi
# diğerini de değiştirir
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)