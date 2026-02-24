
print("Привет, мир!")  # выводим на экран строку через print
a = 5
b = 10
c = 15
print( a, b, c )
print(f"Результат сложения 10 + 25 =", {a +b +c + a})
#2--------------------------
print( 1, 2, 3 , sep = " & ")
print("Python", end =" ")
print("лучший язык")
#------------------------
x = 3.14
y = -8
print(f"Координаты точки: {x}; {y}") # F-строка
# ---------------------------------------------
a = input()
b = int(input())
print(f"имя: {a}, возраст: {b}")
#---------------------------
a = input()
print(f"Привет, {a}!")
a = int(input())
b = int(input())
print(f"{a + b}")
c = int(input())
print(f"{c * c}")
#---------------------------
print(bool(5 > 3)) # True
print(bool(10 < 2)) # False
print(bool(7 == 7)) # True
print(bool(6 != 8)) # True
print(bool(4 >= 4)) # True
print(bool(9 <= 3)) # False
#-----------------
res = 8 > 12
print(res)
print(type(res))
#-------------------------
x = 15
print(x % 2 == 0)
print(x % 3 == 0)
print((x % 3 == 0) or(x % 5 == 0)) # True
#----------------
y = 4.5
print(y >= 1 and y <= 10) # True
print(y >= 0 and y <= 5) or (y >= 10 and y <= 15) # True (так как стоит or)
print(not( y < 5)) # False
#----------------------
print(True or False and False) # True
print(not(False and True)) #True
print(False or not True and True) # False
print(not (10 > 5 or 3 < 1)) # False
#-----------------------------
print(bool(0)) # False
print(bool(-5)) # True
print(bool(3.14)) # True
print(bool("")) # False
print(bool("Python")) # True
print(bool(" ")) # True
#-------------------------
n = 7
print(n > 0)
print(n % 2 ==0)
print(n % 3 ==0)
#-----------------
s = "Программирование"
print(s[1])
print(s[15])
print(s[3])
print(s[len(s)-2])
#----------------------
s =[100]
print(s[len(s)-1])
#-------------------
s = "Программирование"
print(s[0:6])
print(s[len(s)-5:])
print(s[2:7]) # Символы с 3-го по 7-й
print(s[::2])
print(s[::-1])
#---------------------
s = "Программирование"
print(s[::3])
print(s[::2]) # выводим через один
#--------------------
s = "программирование"
s2 = "П" + s[1:]
print("Исходная строка:", s)
print("Новая строка:    ", s2)
#--------------------------------
word = "abcdefgh"
print(word[2:5])
print(word[::-1])
print(word[1:-1])








