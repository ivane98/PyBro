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


###DICTIONARIES

# capitals = {
#     'usa': 'washington',
#     'russia': 'moscow',
# }

# capitals.update({'germany':'berlin'})
# capitals.update({'usa': 'telavi'})
# capitals.pop('russia')
# capitals.clear()

# for key, value in capitals.items():
#     print(key, value)

###INDEX OPERATOR

# name = 'bro Code!'

# # if name[0].islower():
# #     name = name.capitalize()

# print(name[-1])

###FUNCTIONS

# def hello(first_name, last_name, age):
#     print("hello" + first_name + last_name + str(age))
#     print('have a nice a day')

# hello('Bro', 'Code', 21)

###RETURN STATEMENT

# def multiply(num1, num2):
#     return num1 * num2

# x = multiply(6, 8)

# print(x)

###KEYWORD ARGUMENTS

# def hello(first, last):
#     print(first, last)

# hello(first='last', last='first')

###NESTED FUNCTION CALLS

# num = round(abs(float(input('enter a number: '))))

# print(num)

###SCOPE

# name = 'Bro'

# def display_name():
#     # name = 'Code'
#     print(name)

# display_name()
# print(name)

###*ARGS

# def add(*args):
#     sum = 0
#     stuff = list(args)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i

#     return sum

# print(add(1, 2, 3))


###**KWARGS

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# hello(first='Bro', middle='dude', last='Code')

###STRING FORMAT

# print("the {item} jumped over a {animal}".format(animal='cow', item='moon'))

# print('Hello my name is {:^10}. Nice to meet you'.format('Bro'))

# number = 1000

# print('the number is {:e}'.format(number))

###RANDOM

# import random
# cards = [1, 2, 3, 's']
# random.shuffle(cards)

# print(cards)

###EXCEPTION HANDLING

# try:
#     num1 = int(input('enter the first num: '))
#     num2 = int(input('enter the second num: '))
#     res = num1 / num2
# except ZeroDivisionError as e:
#     print(e)
#     print('cant devide by zero')
# except ValueError as e:
#     print(e)
#     print('enter a num please')
# except Exception as e:
#     print('something went wrong')
# else:
#     print(res)
# finally:
#     print('finally')

###FILE DETECTION

# import os

# path = r"C:\Users\TELAVI-PC\Desktop\f"

# if os.path.exists(path):
#     print('file exists')
#     if os.path.isfile(path):
#         print('it is a file')
#     elif os.path.isdir(path):
#         print('it is a folder')
# else:
#     print('file doesnt exist')


###READ A FILE

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('file doent exist')

###WRITE A FILE

# text = 'hello  ee'

# with open('test.txt', 'a') as file:
#     file.write(text)

###COPY A FILE

# import shutil

# shutil.copyfile('test.txt', 'copy.txt')

###MOVE A FILE

# import os 

# os.replace('test.txt', r'\r')

###DELETE A FILE

# import os
# import shutil
# path = 'r'
# shutil.rmtree(path)

###MODULES

# import msg as m

# m.hello()
# m.bye()

###OOP

# class Car:

#     wheels = 4
#     def __init__(self, make, model, year, color) -> None:
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
    
#     def drive(self):
#         print('this car is driving')
    
#     def stop(self):
#         print('this car is stopping')

# car1 = Car('Chevy', 'corvette', 2021, 'blue')
# car2 = Car('Chevy', 'corvette', 2022, 'red')

# class Organism:
#     alive = True

# class Animal(Organism):
#     def eat(self):
#         print('eat')
#         return self

#     def sleep(self):
#         print('sleep')
#         return self

# class Rabbit(Animal):
#     def eat(self):
#         print('rabbit eats')
#         return self

# class Prey:
#     def run(self):
#         print('run')

# class Predator:
#     def hunt(self):
#         print('hunt')

# class Fish(Prey, Predator):
#     pass


# class Rectangle:
#     def __init__(self, length, width) -> None:
#         self.length = length
#         self.width = width

# class Square(Rectangle):
#     def __init__(self, length, width) -> None:
#         super().__init__(length, width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):
#     def __init__(self, length, width, height) -> None:
#         super().__init__(length, width)
#         self.height = height

#     def volume(self):
#         return self.length*self.width*self.height

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def go(self):
#         print('car')

#     def stop(self):
#         print('car stopped')

# class Motorcycle(Vehicle):
#     def go(self):
#         print('motorcycle')

#     def stop(self):
#         print('motorcycle stopped')
    

# # vehicle = Vehicle()
# # car = Car()
# # motorcycle = Motorcycle()

# # # vehicle.go()
# # car.go()
# # motorcycle.go()

# class Carr:
#     color = None

# def change_color(car, color):
#     car.color = color


# class Duck:
#     def talk(self):
#         print('duck walk')
#     def walk(self):
#         print('duck walk')

# class Chicken:
#     def talk(self):
#         print('chicken walk')
#     def walk(self):
#         print('chicken walk')

# class Person:
#     def catch(self, duck):
#         duck.talk()
#         duck.walk()
#         print('catch')

# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)
    
###WALRUS OPERATOR

# print(happy := True)

# normal
# foods = []
# while True:
#     food = input('what food do you like: ')

#     if food == 'quit':
#         break
#     foods.append(food)

#walrus
# foods = []
# while food := input('What foods do you like: ') != 'quit':
#     foods.append(food)

###FUNCTION TO VARIABLE

# def hello():
#     print('hello')

# print(hello)
# hi = hello
# print(hi)

# say = print
# say('hi')

###HIGHER ORDER FUNCTIONS

# def loud(text):
#     return text.upper()

# def quite(text):
#     return text.lower()

# def hello(func):
#     text = func('Hello')
#     print(text)

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend

###LAMBDA

# mult = lambda x, y: x*y
# age_check = lambda age: True if age > 18 else False
# print(age_check(9))

###SORT

# students = [('spongebob', 'A', 99), ('squidward', 'F', 50), ('mr. krabs', 'C', 60)]

# grade = lambda grades:grades[1]

# # students.sort(key=grade, reverse=True)

# sorted_students = sorted(students, key=grade)

# for i in students: 
#     print(i)

###MAP

# store = [1, 2, 3]


# # print(map(store, lambda x: x + 1))

# # Double all numbers using map and lambda

# result = map(lambda x: x*0.8, store)
# print(list(result))

###filter

# friends = [
#     ('one', 21),
#     ('two', 17)
# ]

# age = lambda age: (age[1] > 18)

# drinking_buddies = list(filter(age, friends))

# print(drinking_buddies)


###reduce

# from functools import reduce

# letters = ['h', 'e', 'l', 'l', 'o']
# word = reduce(lambda x, y: x + y, letters)

# numbers = [1, 2, 3, 4, 5]

# factorial = reduce(lambda x, y: x*y, numbers)

# print(factorial)

###list comprehension

# nums = [1, 2, 3, 4]

# filt = [i if i > 2 else 'F' for i in nums ]

# print(filt)

###dict comprehension

# cities_in_f = {'a': 10, 'b': 12, 'c': 13}

# only_sunny = {key: ('warm' if value > 10 else 'cold') for(key, value) in cities_in_f.items()}

# print(only_sunny)

###zip function

# usernames = ['1', '2', '3']
# passwords = ['a', 'b', 'c']

# users = dict(zip(usernames, passwords))

# print(users)

###if _name_ == '__main__'

# def hello():
#     print('hello')


# if __name__ == "__main__":
#     hello()

###time module

# import time

# # print(time.ctime(0))

# print(time.localtime())


 



