
####################################
###functions
# def greeting(n):
#     if n==1:
#         print("hello world")
#     if n>1:
#         print("hello 2 worlds")

# greeting(1)
    

# def printnames():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# printnames()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# printnames()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# printnames()

# def myfunc():
#     for i in range (10):
#         print(i)


# myfunc()

# def greeting(person):
#     print(f'hello {person}')

# greeting("100.00/2")
# greeting(99/5)
# greeting([1,2])


# def add(n1, n2):
#     s=n1+n2
#     print(s)
#     return s

# add(4, 5)
# S = add(4, 5)
# print(S)

# def cal_avg():
#     sum=0
#     l=[]
#     # l=[1, 3, 10, 10, 5]
#     n = int(input("Enter Numbers of Element"))
#     for i in range(n):
#         ele = int(input())
#         l.append(ele)

#     for i in range(len(l)):
#         sum = sum + l[i]

#     avg = sum/len(l)
#     print(avg)

#     return avg


# cal_avg()


# def myFunc (n1, n2, n3):

#     return n1*2, n2*3, n3*4

# # result = myFunc(4, 7, 9)

# c1, c2, c3 = myFunc(4, 7, 9)

# # print(type(result))

# print(c1)
# print(c2)
# print(c3)

# def dance():
#     kind = "silly"
#     print("I am doing a %s dance" % kind)
#     print(kind)
# dance()

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# helloIs = my_dictionary["hello"]
# print(helloIs)

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# watIs = my_dictionary.get("wat")
# print(watIs)

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# my_dictionary["theMeaningOfLife"] = "wat"
# wat = my_dictionary["theMeaningOfLife"]
# print(wat)

# my_dictionary["newKeyName"] = "hello world"
# print(my_dictionary)
# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# # items = my_dictionary.items()
# # print(items)
# print(my_dictionary)

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# watIs = my_dictionary.get("hello")
# print(watIs)

# def test_f():
#     print("hahahahha")

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
#     # 2 : testf()
# }
# values = my_dictionary.values()
# print(values)

# print(my_dictionary[0])

# my_dictionary = {
#     "hello" :   "world",
#     "sqareOfTwo" : 4,
#     "theMeaningOfLife" : 42,
#     0 : 1
# }
# for key, value in my_dictionary.items():
#     print(key)
#     print(value)

# s = 7.1%1*100

# print(s)


# contacts = [{
#     "fn":"Rich",
#     "ln":"Z"},
#     {"fn":"AA",
#     "ln":"Bb"},
#     {"fn":"CC",
#     "ln":"Cd"},]

# print(contacts[0]["fn"])

# import pickle
# import os.path
    

# if os.path.isfile('data.pickle'):
#     with open('data.pickle', 'rb') as fh:
#         phonebook = pickle.load(fh)
# else:
#     print ("File not exist")
#     phonebook = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
#     }

# def phone_book_app():
#     print("By using the phone book, please enter the options:")
#     print("1, Look up and entry")
#     print("2, Set an entry")
#     print("3, Delete an entry")
#     print("4, List all entries")
#     print("5, Quit")
#     entry=input("Please enter your option: ")

#     if entry == '1':
#         name = input("Enter the name of the person: ")
#         result = phonebook.get(name)
#         print(result)

#     if entry == '2':
#         name = input("Enter the name of a new person: ")
#         number = input("Enter the phone number of the person xxx-xxx-xxxx  :")
#         phonebook[name] = number
#         print(f"New Entry has entered: {name} with number {number}")
    
#     if entry == '3':
#         name = input("Enter the name of the person with number to delete: ")
#         del phonebook[name]
    
#     if entry == '4':
#         print(phonebook)
    
#     if entry == '5':
#         print("Bye! ")
#         exit()

# phone_book_app()
# with open('data.pickle', 'wb') as fh:
#     pickle.dump(phonebook, fh)
# # print(phonebook)


# myList = [1,2,3,4]
# myNewList = myList
# myNewList[1] = 77

# print(myList)

# class Greeting:
#     def say_hello(self):
#         print('Hello')
    
# newGreetingObj = Greeting()

# newGreetingObj.say_hello()

# class Student:
#     def __init__(self,name, lname):
#         self.name = name ###(is instance variable)
#         self.lname = lname
#         print(f'Good morning, {self.name.capitalize()} {self. lname.capitalize()}.')

#     def greeting(self):
#         print("Good morning!")

# alina = Student('alina','belova')

# sean = Student('sean','page')




# print(alina.name.capitalize()+' '+alina.lname.capitalize())
# print(sean.name + sean.lname)


# class MyClass:
#     def __init__(self):
#       print("Upon Initialization: Hello!")   ###(is instance variable)
#     def instance_method(self): 
#       print("hello instance")
#     def class_method():
#       print("Hello class method!")
# test = MyClass()
# # test.instance_method()
# # MyClass.class_method()

# class Animal:
#   def __init__ (self, name):
#     self.name = name


# dog = Animal('dog')

# cat = Animal('cat')

# horse = Animal ('horse')

# print(dog.name)
# print(cat.name)
# print(horse.name)


# import datetime

# class Person:
#     def __init__(self, fname, lname, bday, address, email):
#         self.fname=fname
#         self.lname=lname
#         self.bday=bday
#         self.address=address
#         self.email=email
#         print(f'{fname} {lname} birthday is {bday}')

#     def age(self):
#         today = datetime.date.today()
#         print(today)
#         age = today.year-self.bday.year

#         if today < datetime.date(today.year, self.bday.month,self.bday.day):
#             age -=1
        
#         return age




# sammy = Person("Sammy","Kry",datetime.date(1998,8,21), "123 street", "sammy@gmail.com")

# age=sammy.age()

# print(age)
# count=0

# def greeting(name):
#     print(f'hello{name}')
#     count += 1
#     print(count)

# greeting("Daniel")
# greeting("Alex")
# greeting("John")
# greeting("Daniel")


# class Person:
#     def __init__(self, name):
#         self.name=name
#         self.count=0        
    
#     def greeting(self):
#         print(f"Hello, {self.name}")
        
    
#     def printCount(self):
#         self.count += 1
#         print(self.count)

# alina = Person("alina")

# alina.greeting()
# alina.greeting()
# alina.greeting()
# alina.printCount()

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print('Hello {other_person.name}, I am {self.name}!')

# Sonny = Person("Sonny", "sonny@hotmail.com","483-485-4948")
# Jordan = Person( "Jordan","jordan@aol.com","495-586-3456")


# Sonny.greet(Jordan)
# Jordan.greet(Sonny)

# print(f"My name is {Sonny.name}, my email is {Sonny.email}, my phone is {Sonny.phone}")
# print(f"Other Person's name is {Jordan.name}, my email is {Jordan.email}, my phone is {Jordan.phone}")


# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0

#   def greet (self):
#     self._greet()

#   def _greet (self):
#     self.count += 1
#     if self.count > 1:
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print("Hello", self.name)

#   def __reset_count(self):
#     self.count = 0

# alex = Person("alex")

# alex.greet()
# alex.greet()
# alex.greet()
# alex._greet()


## Inheritance

# #Hello
# #olleH

# class vString(str):
#     def reverse(self, name):

#         rstring =""

#         for char in name:
#             rstring = char + rstring

#         return rstring
    
# myString = vString("Hello")

# print(myString.capitalize())

# reversed = myString.reverse("hello")

# print(reversed)

################## implicit
# class Parent():
#     def implicit(self):
#         print("PARENT implicit()")
# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

################ ovewrride

# class Parent(object):
#     def override(self):
#         print("PARENT override()")
# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
# dad = Parent()
# son = Child()
# dad.override()
# son.override()
########################### alter ???
# class Parent():
#     def altered(self):
#         print("PARENT altered()")

# class Child(Parent):
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         # super(Child, self).implicit()  ##### super can call upper parent method
#         # super(Child, self).implicit()
#         print("CHILD, AFTER PARENT altered()")



# dad = Parent()
# son = Child()
# dad.altered()
# son.altered()
##########################################
# class Character:
#     def __init__(self, name, power, health):
#         self.name = name
#         self.power = power
#         self.health = health

    
# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero,self).__init__(name, power, health)

# alina = Hero("pink gun","alina",3,10)
# print(alina.weapon)
# print(alina.name)


##########################################
# ##Class work:

# class Vehicle:
#     def __init__(self,make, model, year):
#         self.make =make
#         self.model=model
#         self.year=year

# car = Vehicle('Nissan', 'Leaf', 2015)
# print(car.make, car.model, car.year)

######################

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print('Hello {other_person.name}, I am {self.name}!')

#     def print_contact_info(self):
#         print(f"{self.name}'s email: {self.email}, {self.name}'s phone: {self.phone}")


# Sonny = Person("Sonny", "sonny@hotmail.com","483-485-4948")
# # Jordan = Person( "Jordan","jordan@aol.com","495-586-3456")

# # Sonny.greet(Jordan)
# # Jordan.greet(Sonny)

# Sonny.print_contact_info()

######################

# ## Add and instance with add_friend
# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.friendList =[]
    
#     def add_friend(self, friend):
#         self.friend = friend
#         self.friendList.append(friend)
#         print(len(self.friendList))
#         print(self.friendList)

#     def add_number_of_friends(self, friends):
#         self.friends = friends
#         self.friendList +=  friends
#         print(len(self.friendList))
#         print(self.friendList)

    

    
#     # def add_friend(self, friend)


# Sonny = Person("Sonny")
# Sonny.add_friend("Jordan")
# Sonny.add_friend("Daniel")

# Sonny.add_number_of_friends(("Mat", "Cloe", "David"))



#################
### count greetings

# class Person:
#     def __init__(self, name):
#         self.name=name
#         self.count=0

#     def greeting(self):
#         print(f"Hello, {self.name}")
#         self.count += 1
        
    
#     def printCount(self):
        
#         print(self.count)

# sonny = Person("sonny")

# sonny.greeting()
# sonny.greeting()
# sonny.greeting()
# sonny.printCount()

#########################

# class Student():
    
#     def __init__(self, firstName, lastName, campus):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.campus = campus
        
        
#     def printStudent(self):
#         print(f"{self.firstName} {self.lastName} campus: {self.campus}")
        
        
    
# class Campus():
#     def __init__(self):
#         self.students = []
        
#     def addStudent(self, firstName, lastName, campus):
#         temp  = Student(firstName, lastName, campus)
#         self.students.append(temp)
        
#     def printSomeStudent(self, index):
        
#         print(self.students[index])
#         return self.students[index]
        
#     def showCurrentStudent(self):
#         for studentObject in self.students :
#             print(f"{studentObject.firstName} {studentObject.lastName} campus: {studentObject.campus}")


# houston = Campus()
# houston.addStudent("alina", "belova", "houston")
# houston.addStudent("kazim", "sha", "houston")
# houston.addStudent("alex", "fisher", "new york")
# houston.addStudent("matt", "ryan", "chicago")
# houston.addStudent("sean", "page", "chicago")

# houston.showCurrentStudent()
#############################################

# class AccountHolder:
    
#     def __init__(self, fname, lname, mname, atype, status, balance):
        
#         self.first_name = fname
#         self.last_name = lname  
#         self.middle_name = mname 
#         self.account_type = atype  
#         self.status = status
#         self.balance = balance

# class Bank:
    
#     def __init__(self, name, address):
#         self.name = name  
#         self.address = address 
#         self.accounts = []
        
#     def open_new_account(self, fname, lname, mname, atype, status, balance):
#         if balance >= 100 :
#             # create a account holder
#             temp = AccountHolder(fname, lname, mname, atype, status, balance)
            
#             # store new account holder in account list
#             self.accounts.append(temp)
            
#             # return "Account created for fname lname"
#             return f"A {atype} account was created for  {fname} {mname} {lname} with a balance of {balance}"
            
#         else:
#             # return "Insufficient deposit amount"
#             return "Insufficient funds.  You need at least $100 to open an account"
    
#     def show_account_holders(self):
        
#         for account_holder_obj in self.accounts:
#             print(f'{account_holder_obj.first_name} {account_holder_obj.last_name} {account_holder_obj.balance}')
            

# # definition of main that includes a while loop with menu of things

# def main():
#     wellsfargo = Bank("wells fargo", "123 sesame street")
#     action = 1
    
#     while action != 6:ls
#         print("1. Create an account")
#         print("2 Print list of all account holders")
#         print("6. Exit application")
        
#         action = int(input("What would you like to do?"))
        
#         if (action == 1):
            
#             fname = input("What is the first name? ")
#             mname = input("What is the middle name?")
#             lname = input("What is the last name?")
#             atype = input("What would like to open? Checking or Savings")
#             deposit = int(input("How much would you like to deposit?"))
            
            
#             response = wellsfargo.open_new_account(fname, lname, mname, atype, "new", deposit)
#             print(response)
#         elif (action == 2):
#             wellsfargo.show_account_holders()
        
#         elif (action == 6):
#             break
        

# # main()

# main()

# Module: https://dc-exxon-slides.netlify.com/python/modules#1

from random import choice # or can be "from (modules(a py file) import fuction"
places = ["McDonalds", "KFC", "Burger King", "Taco Bell","Wendys", "Arbys", "Pizza Hut"]
def pick():  # see the docstring below?
    return choice(places)
print(f"let's go to {pick()}")
# or import "../myFolder/random"