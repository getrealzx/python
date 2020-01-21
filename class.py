
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

import pickle
import os.path
    

if os.path.isfile('data.pickle'):
    with open('data.pickle', 'rb') as fh:
        phonebook = pickle.load(fh)
else:
    print ("File not exist")
    phonebook = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
    }

def phone_book_app():
    print("By using the phone book, please enter the options:")
    print("1, Look up and entry")
    print("2, Set an entry")
    print("3, Delete an entry")
    print("4, List all entries")
    print("5, Quit")
    entry=input("Please enter your option: ")

    if entry == '1':
        name = input("Enter the name of the person: ")
        result = phonebook.get(name)
        print(result)

    if entry == '2':
        name = input("Enter the name of a new person: ")
        number = input("Enter the phone number of the person xxx-xxx-xxxx  :")
        phonebook[name] = number
        print(f"New Entry has entered: {name} with number {number}")
    
    if entry == '3':
        name = input("Enter the name of the person with number to delete: ")
        del phonebook[name]
    
    if entry == '4':
        print(phonebook)
    
    if entry == '5':
        print("Bye! ")
        exit()

phone_book_app()
with open('data.pickle', 'wb') as fh:
    pickle.dump(phonebook, fh)
# print(phonebook)
