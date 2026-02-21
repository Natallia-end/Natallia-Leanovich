name = "Natallia"
age = "35"
height = "1.64"
print("Имя:", name) # Имя
print("Возраст:", age) # Возраст
print("Рост:", height) # Рост
# --------------------------------------
x = 10
print(x)
print(type(x)) # class "int"

x = 25.5
print(x)
print(type(x)) # class "float"

x = "python"
print(x)
print(type(x)) # class "str"
# ----------------------------------------
a = 7
b = a
print("a=", a)
print("b=", a)
a = 10
print("b=", b) # Переменная b продолжает ссылаться на старый объект 7
print("Переменная b продолжает ссылаться на старый объект 7")
#------------------------------------------
x=y=z=100
print("Значения после каскадного присваивания:")
print("x=", x)
print("y=", y)
print("z=", z)

print("Id после каждого присваивания")
print("id(x)=", id(x))
print("id(y)=", id(y))
print("id(z)=", id(z))

if id(x) == id(y) == id(z):
    print("Проверяем все id одинаковы - переменные ссылаются на один объек ")
else: print("id разные - переменные ссылаются на разные обьекты")
#-----------------------------------------
a = 5
b = 10
print("До обмена чисел:")
print("a=",a)
print("b=",b)
print("После обмена:")
print("a=",a)
print("b=",b)
#----------------------------------------
import keyword
print(keyword.kwlist)
print("True, print, if - уже используются в pyhton.")
#--------------------------
var1 = 42
var2 = 3.14
var3 = "Привет"
print(type(var1))
print(type(var2))
print(type(var3))

var1 = "круг"
print(type(var1))
#------------------------
name = "Inna"
age = 20
height = 1.70
weight = 59
language = "python"

print(("Имя:"), name, type(name))
print(("Возраст:"), age, type(age))
print("Рост:", height, type(height))
print("Вес:", weight, type(weight))
print("Язык:", language, type(language))