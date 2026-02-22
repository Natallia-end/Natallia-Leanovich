s1 = "Python"
s2 = "Программирование"
print(s1)
print(s2)
s3 = """Python
Программирование
"""
print(s3)
a = ""
s4 = len(a)
print(s4)
#------------------------
s1 = "Иван"
s2 = "Петров"
s3 = "Иван Петров"
s4 = s1 + " " + s2
print(s4)
#-------------------------
s = "Возраст:"
age = 25
s1 = s + str(age) # Объединяем строку s и число age, используя str()
print(s1)
#--------------------------
s1 = "ха"
s2 = (s1 + " " ) * 5
print(s2)
"""s3 = (s1 + " " ) * 2.5 # Можно умножать строку только на целое число (тип int)
print(s3)"""
#------------------------
text = "Привет, мир!"
s1 = len(text)
print(s1) # Выведим длину строки
text1 = ""
s2 = len(text1)
print(s2)
#--------------------------------
sentence = "Я изучаю Python" # проверяем ли содержится в sentence "Python"
print("Python" in sentence) # True
print("Java" in sentence) #False
#-------------------------------------
a = "apple"
b = "banana"
print(a == b) #False
print(a != b) #True
print(a < b) #True
print(a <= b) #True
print(a >= b) #False
#----------------------
print(ord("A")) #65
print(ord("a")) #97
print(ord("Я")) #1071
#----------------------








