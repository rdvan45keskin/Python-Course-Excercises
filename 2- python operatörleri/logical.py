x = 5
hak = 5
devam = "e"
result = 5 <= x < 10
# and
result = (x > 5) and (x < 10)   #true,true = true
result = (hak > 0) and (devam == "e")
#or
result = (x>0) or (x % 2 ==0)   #true, false => true
#not
result = not(x>0)
print(result)