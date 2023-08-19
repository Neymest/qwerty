#print("Результат: ", 7, 15, 228, sep="", end="\n")
#print("Second Line: 7, 15, 228")
#input("Введите свой возраст: ")
#input("Введите свой город: ")
#input("Кек?")

#number = (199 + 5) * 20
#word = "Результат:"
#print(word, number)
#number = 5000
#digit = -5
#print(word, number)
#print(number + digit)

#num1 = int(input("Введите первое число: "))
#num2 = int(input("Введите второе число: "))

#num1 += 2
#num1 -= 5

#print("Результат", num1 + num2)
#print("Результат", num1 - num2)
#print("Результат", num1 / num2)
#print("Результат", num1 * num2)
#print("Результат", num1 ** num2)
#print("Результат", num1 // num2)

#word = "Привет"
#print(word * 2)
#word = True

#if 10 > 5:
    #print("Da")

#isHappy = False
#if isHappy or user_data == 6:      #if vsegda v nachale
#    print("User is happy")
#elif user_data == 5:        #elif vsegda po seredine
#    print("Number is 5")
#elif user_data == 7:
#    print("Number is 7")
#else:                      #esle vsegda v konce, no mozhno i bez nego
#    print("User is unhappy")

#if user_data != 5:
#    print("тута")
#    if user_data > 6:
 #      print("число больше 6")

#data = input()

#number = 5 if data == "Five" else 0 #to zhe samoe chto nizhe tol'ko 1 str
#if data == "Five":
#    number = 5
#else:
#    number = 0

#for i in range(-2, 6, 1):
    #print(i)

#count = 0
#word = "Hello World!"
#for i in word:
#    if i == "l":
#        count += 1
#print("Count:", count)


#isHasCar = True

#while isHasCar:
#    if input("Enter data: ") == "Stop":
#        isHasCar = False

#for i in range(1, 11):
#    if i == 5:
#        break
#    if i % 2 == 0:
#        continue
#    print(i)

#for i in "hello":
#    if i == "r":
#        found = True
#        break
#else:
#    found = False
#print(found)

#nums = [5, 7, 2, 4, 7, True, "Hello",6.7, [5, 7, 8]]

#nums[0] = 50
#nums[5] = 10
#print(nums[-1][])
#numbers = [5, 2, 7]
#numbers.append(100)

#nums = [5, 2, 7, "50", False]
#for el in nums:
#    el *= 2
#    print(el)

#n = int(input("Enter length: "))

#user_list = []
#i = 0
#while i < n:
#    string = "Enter element #" + str(i + 1) + ": "
#    user_list.append(input(string))
#    i += 1
#print(user_list)

#word = 'kostya petuh, govnoed, sobaka'
#print(word.count('p'))
#print(word.capitalize())
#print(word.find('pet'))
#print(word.split(', '))
#hobby = word.split(', ')

#for i in range(len(hobby)):
#    hobby[i] = hobby[i].capitalize()
#result = ", ".join(hobby)
#print(result)

#word = 'Football'
#print(word[4:])

#lis = [6, 4, "Stroka", True, 6.5]
#print(lis[2:])
#print(lis[::])

#data = (4, 6, 7, 3, 6, True, 5.5, 'Privet')
#data[0] = 5 - no
#print(data[::])
#print(data)

#data = (4, 6, 7, 3, 6, True, 5.5, 'Privet')
#for el in data:
#    print(el)
#nums = [5, 6, 7]
#new_data = tuple(nums)
#word = tuple('Hello world')
#print(word)

                    # dict slovari
#country = {'code': 'UA', 'name': 'Ukraine', 'population': 28}
#country = dict(code='UA', name='Ukraine')
#print(country['name'])
#print(country.items())
#for key, value in country.items():
#    print(key, " - ", value)

# klyuchi(keys) v slovaryah
#country = {'code': 'UA', 'name': 'Ukraine', 'population': 28}
#print(country.get('name'))
#country.pop('name')
#country['code'] = 'None'
#print(country)

                #Описание человека через словарь и ключи
#person = {
#    'user_1': {
#        'first_name': 'John',
#        'last_name': 'Green',
#        'age': 25,
#        'address': ['c.NK', 'st.Trub', '228' ]
#    },
#    'user_2': {
#        'first_name': 'Dasha',
#        'last_name': 'Green',
#        'age': 22,
#        'address': ['c.NK', 'st.Trub', '228' ]
#    }
#}
#print(person['user_1'])
#print(person['user_2'])


#ata = set('hello')

                   # MNOZHESTVA
#data = {5, 7, 4, 3, 5}
#data.add(32)
#data.update(['32', True, 6, 8])
#data.remove(True)
#data.pop()
#data.clear()

#nums= [5, 7, 3, 5, 5, 5, 7]
#nums = set(nums)

#new_data = frozenset([2, 3, 5, 7, 1, 4, 3, 5, 7])

#print(new_data)

                     #Sozdanie funkcii

#def test_func(word):
#    print(word, end="")
 #   print("!")


#test_func(5)
#test_func(228)

#def summa(a, b):
#    res = a + b
 #   #print("Result: ", res)
  #  return res or a + b

#res = summa(5.2, 7.6)
#print(res)
#summa(5.2,7.6)
#res2 = summa("H", "i")
#print(res2)

#nums1 = [5, 7, 9, 4]

#min = nums1[0]
#for el in nums1:
#    if el < min:
#       min = el
#print(min)

#def minimal(L):
#   min_number = L[0]
#   for el in L:
#       if el < min_number:
#           min_number = el
#   return min_number
#nums1 = [5, 7, 2, 9, 4]
#min1 = minimal(nums1)
#nums2 = [5, 7, 2, 9, 4, 1, 2, 3, 4, 5, 0, -2, -55, -200]
#min2 = minimal(nums2)
#if min1 < min2:
#    print(min1)
#else:
#    print(min2)

#Anonimnaya funkciya, men'she strok
#func = lambda x, y: x * y
#print(func(5, 2))
               #Rabota s failami
#data = input("Введите текст: ")
#file = open('data/text.txt',  'a')
#file.write(data + "\n")
#file.close()

#file = open('data/text.txt', 'r')

#print(file.read())

#for line in file:
#    print(line, end="")


#file.close() VSEGDA PROPISIVAT' !!!!!!!!!!

#Обработчик исключений. Конструкция try - except
#try:
#    x = int(input("Введите число:"))
#    x += 5
#    print(x)
#except ValueError:
#    print("Введите лучше число!")

#x = 0
#while x == 0:
#    try:
#        x = int(input("Введите число:"))
#        x += 5
#        print(x)
#    except ValueError:
#        print("Введите лучше число!")

#try:
#    x = 5 / 1
#    x = int(input())
#except ZeroDivisionError:
#    print("Деление на ноль!")
#except ValueError:
#    print("Вы ввели что-то не так")
#else:                     #работает только если выполнился трай,а не эксепты
#    print("else")
#finally:
#    print("Finally")

#with / as
#file = open('text.txt, 'r')
#file.read()
#file.close()
#try:
#    with open('data/text.txt', 'r', encoding='utf-8') as file:
#        print(file.read())
#except FileNotFoundError:
#    print("Файл не найден")

# MODULI
#import time
#time.sleep(3)
#print("hello")

#import datetime as d
#print(d.datetime.now().time())

#import datetime as d, sys, os, platform
#import random, array(massiv), math(mat funkcii)
#print(platform.system())

#import math
#from math import sqrt as s, ceil
#print(ceil(s(25)))

# mymodule as my
#print(my.name)
#my.hello()

#from mymodule import add_three_numbers as a3n
#print(a3n(5, 3, 6))

#Kachaem biblioteki cherez pypi site, ustanovka cherez terminal
#import cowsay as cs
#cs.cow('Hello')

#OSNOVI OOP. SOZDANIE KLASSA I OBJEKTA

#class Cat:
#    name = None
#    age = None
#    isHappy = None
#some = [], {}, ()
#    def __init__(self, name, age, isHappy):
#        self.set_data(name, age, isHappy)
#        self.get_data()

#    def set_data(self, name = None, age = None, isHappy = None):
#        self.name = name
#        self.age = age
#        self.isHappy = isHappy
#    def get_data(self):
#        print(self.name, "age:", self.age, ". Happy:", self.isHappy)

#cat1 = Cat("Alice", 1, True)
#cat1.set_data("Alice", 1, True)
#cat1.set_data()
#cat2 = Cat("Tofi", 1, False)
#cat2.set_data("Tofi", 1, False)
#cat1.get_data()
#cat2.get_data()

#NASLEDOVANIE
#class Building:
#    __year = None
#    __city = None
#
#    def __init__(self, year, city):
#        self.year = year
#        self.city = city

#   def get_info(self):
#        print("Year:", self.year, ". City:", self.city)

#class School(Building):
#    pupils = 300
#
#    def __init__(self, pupils, year, city):
#        self.pupils = pupils
#        super(School, self).__init__(year, city)
#    def get_info(self):
#        super().get_info()
#        print("Pupils:", self.pupils)

#class House(Building):
#    pass
#class Shop(Building):
#    pass

#school = School(300, 2000, 'Nikopol')
#school.get_info()
#house = Building(2000, 'Nikopol')
#house.get_info()
#shop = Building(2000, 'Nikopol')
#shop.get_info()

# DEKORATORI FUNKCII

#import webbrowser

#def validator(func):
#    def wrapper(url):
#        if "." in url:
#             func(url)
#        else:
#            print("Wrong url")
#    return wrapper

#@validator
#def open_url(url):
#    webbrowser.open(url)

#open_url("youtube.com")

#MIMO TESTI
#old_password = "hello123"
#new_password = "goodbye321"
#compare_old_new = old_password != new_password
#repeat_new_password = "goodbye321"
#compare_new = new_password == repeat_new_password

#print(f"Is new password different from old password? {compare_old_new}")
#print(f"Has new password been introduced correctly? {compare_new}")

#read = 5
#unread = 4
#if unread != 0:
#   print(f"You have {unread} unread messages")
#else:
#    print(f"No unread messages. Check your {read} read messages")

#actualPass = "abc123"
#enteredPass = "Abc123"
#if actualPass == enteredPass:
#    print("Login successful.")
#else:
#    print("Incorrect credentials. Please try again.")

#age = 21
#hasReservation = True
#result = False

#if age >= 18 and hasReservation:
#    result = True
#print(f"Entry granted: {result}")

#sales = 0
#inventory = 10
#sales += 1
#inventory -= 1

#print(f"Sales: {sales}")
#print(f"Inventory: {inventory}")

#students_names = "Samantha,Mcgrath,Peyton,Kerim,Nadia,Sandra,Sarah,Alex"
#names_list = students_names.split(",")
#print(names_list)

#tech_stack = "Angular Node Mongo Express"
#tech_stack = tech_stack.replace("Angular", "React")
#tech_stack_list = tech_stack.split()
#print(tech_stack_list)


