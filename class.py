# # name = "Richard"
# # lname = "Zhang"

# # output = "good mornining {0} {1} {1}{1}{1}".format(name, name)

# # # print(output)
# # s1="john"
# # s2="adfa"
# # output = f'hello richard {s1} {s2}'
# # print (isinstance(s1, str))
# # import math

# yourage = input("Enter your Age:   ")

# numage = int(yourage)
# dataType = type (numage)
# output = f'you are {yourage} '
# print(output)
# print(dataType)

# age = 26
# if (age == 25) :
#     print(age)

# name = input("Enter in your name >>")
# if (name == "Richard") :
#     print(name)

# Aage = input("What is your Age?")
# age = int(Aage)
# if age >= 21:
#   print("You get free beer")
# elif age < 18:
#   print("What are you even doing here?")
# else:
#   print("Sorry no beer for you")


# greeting = "Hello {}, it is very nice to meet you and your friend {}!"
# salute = "{}, you are the hero, you don't have any friends alive!"
# name_of_user = input("What is your name? ")

# length_of_name = len(name_of_user)

# if name_of_user == "Richard":
#     print(salute.format(name_of_user))

# elif length_of_name > 0:
#     name_of_friend = input("What is your friend's name? ")
    
#     print(greeting.format(name_of_user,name_of_friend))


# else:
#     print("OK, I'll ask again some other time.")



# count = 0
# while count < 10:
#     print ('the count is', count)
#     count += 1
#     print ('the count after is', count)
# print ("done")


answer =""
while answer != "when":
    answer = input ('Say when: ')
    answer = answer.lower()
print("You got it!")