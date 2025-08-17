# global scope
x = "global x"

def function():
    #local scope
    x = "local x"
    print(x)

function()
print(x)

#############################
# global
name = "Rıdvan"

def changeName(newName):
    # local
    name = newName
    print(name)
changeName("Indigo")
print(name)

####################
name = "global string"

def greeting():
    # name = "Rıdvan"

    def hello():
        # name = "Indigo"
        print("hello "+name)
    hello()

greeting()

#####################

x = 50
def test():
    global x
    print(f"x {x}")

    x = 100
    print(f"changed x to {x}")
test()
print(x)

# fonksiyonun içindeki değer ile dışardaki değer farklı adreste tutulur
# bu nedenle fonksiyonun içinde dıştaki değeri değiştirecek işlem yapılsa dahi
# bu sadece fonksiyonun içinde geçerlidir dışardaki değişken dışarıda print ile
# yazdırılırsa hala ilk değerini korur.
# ama global ile dışardaki bilgiyi fonksiyonda değiştirirsek dışardaki de değişir