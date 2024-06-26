#VARIABLES

# first_name = 'ivane'
# last_name = 'Vardoshvili'

# full_name = first_name + " " + last_name

# print(full_name)

# age = 25
# age +=1

# print('here is my age:' + str(age))

#same stuff for floats and bools

# name, age, attractive = 'ivane', 25, True

# spongebob = squidward = sandy = patric = 30

# print(spongebob, squidward, sandy, patric)

# STRINGS

# name = 'Bro'

# print(name)
# print(len(name))
# print(name.find("I"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("i"))
# print(name.replace("o", "a"))
# print(name*10)

# TYPECASTING

# x = 1
# y = 2.0
# z = '3'

# x = str(x)
# y = str(y)
# z = str(z)

# print(x)
# print("hello:" + y)
# print(z*3)

###User Input

# name = input("What is your name: ")
# age = int(input('How old are you: '))
# height = float(input("What is your height: "))

# print("Hello " + name)
# print("you are " + str(age) + " years old")
# print("your height is " + str(height) + " cm")


##Math Funcs

# import math

# pi = 3.14
# x = 2

# print(round(pi))
# print(math.floor(pi))
# print(math.ceil(pi))
# print(abs(pi))
# print(max(pi, x))
# print(min(pi, x))
# print(math.sqrt(pi))


###String Slicing

# name = "Bro Code"

# print(name[0:4])
# print(name[4:])
# print(name[::-1])

# website1 = "https://www.google.com"
# website2 = "https://www.wikipedia.com"

# slc = slice(12, -4)

# print(website2[slc])

##If, Else, Elif

# age = int(input("How old are you: "))

# if age == 100:
#     print('you are century old')
# elif age >= 18:
#     print("you are an adult")
# elif age < 0:
#     print("you are not born")
# else:
#     print("you are a child")

###Logical Operators

# temp = int(input("Input Temp: "))

# if not(temp >= 0 and temp <= 30):
#     print("temp is good go outside")
# elif not(temp < 0 or temp > 30):
#     print("temp is bad dont go outside")

###While Loop

# name = None

# while not name:
#     name = input('Enter your name')

# print("hello " + name)

###For Loop

# import time

# # for i in range(10):
# #     print(i + 1)

# # for i in range(50, 100+1):
# #     print(i)

# # for i in "Bro Code":
# #     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)

# print("Happy new year")

###Nested Loops

# rows = int(input('Enter rows: '))
# cols = int(input('Enter cols: '))
# symbol = input('Enter symbol: ')

# for i in range(rows):
#     for i in range(cols):
#         print(symbol, end='')
#     print()

###Loop Control Sequence

# while True:
#     name = input("Enter your name")
#     if name != "":
#         break

# phone = '123-456-789'

# for i in phone:
#     if i == "-":
#         continue
#     print(i, end='')

# for i in range(1, 21):
#     if i == 13:
#         pass
#     print(i, end='')

###LISTS

# food = ['pizza', 'hamburger', 'hotdog', 'spaghetti']

# food[0] = 'suchi'

# food.append('pudding')
# food.remove('hotdog')
# food.pop()
# food.insert(0, 'cake')
# food.clear()
# print(food)

###2D LISTS

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]


# nums = [x, y, z]

# print(nums[0][0])

###TUPLE

# student = ('Bro', 21, "male")

# print(student.index('Bro'))
# print(student.count('Bro'))

# for i in student:
#     print(i)

# if "Bro" in student:
#     print("Bro is here")

###SETS

# utensils = {"fork", "spoon", "knife", "knife"}
# dishes = {'bowl', 'plate', 'cup', 'knife'}
# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()

# dishes.update(utensils)

# dinner_table = utensils.union(dishes)

# for i in dishes:
#     print(i)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))