
# #1. Tip Calculator


# import math

# bill = float(input("Total bill amount? "))
# lvlsvs = input("Level of Service? ")
# lvlsvs = lvlsvs.lower()
# print(lvlsvs)

# percenttips = 0.1

# if lvlsvs == "good":
#     percenttips = 0.2
# elif lvlsvs == "fair":
#     percenttips = 0.15
# elif lvlsvs == "bad":
#     percenttips = 0.1



# tips = float("%.2f" %(percenttips * bill))
# total = bill + tips

# output = f"Tip amount is ${tips} \nTotal amount is ${total}"

# print(output)
##########################

#Tip Calculator 2


bill = float(input("Total bill amount? "))
lvlsvs = input("Level of Service? ")
lvlsvs = lvlsvs.lower()
n_ppl = int(input("Split how many ways? "
))
print(lvlsvs)

percenttips = 0.1

if lvlsvs == "good":
    percenttips = 0.2
elif lvlsvs == "fair":
    percenttips = 0.15
elif lvlsvs == "bad":
    percenttips = 0.1



tips = float("%.2f" %(percenttips * bill))
total = bill + tips
amount_per_person = float("%.2f" %(total / n_ppl))

output = f"Tip amount is ${tips} \nTotal amount is ${total} \n Amount per person: ${amount_per_person}"

print(output)
##########################









# #first 100 triangle number
# count = 0
# tn = 1 #tn is triangle number
# while count < 100:
#     count +=1
#     tn = count*((count+1)/2)
#     print(tn)
# print("those are first 100 triangle numbers")

#Factor Numbers

# asknum = input("please input a number >>")
# x = int(asknum)
# i = 1
# print("the factor(s) of", x, "are")
# while i < x:
#     if x % i ==0:
#         print(i)
#     i +=1
    
#Guess a Number
# #Guess a Number V1
# print("I am thinking of a number bewteen 1 and 10")

# gn = 0
# while gn != 5:
#     gn = int(input("What's the number?"))

# print("Yes! You win!")



# #Guess a Number V2
# print("I am thinking of a number bewteen 1 and 10")
# setnumber = 5
# gn = 0
# while gn != setnumber:
#     gn = int(input("What's the number?"))
#     if gn > setnumber:
#         print(gn, " is too hight")
#     if gn < setnumber:
#         print(gn, " is too low")

# print("Yes! You win!")


# #Guess a number v3

# import random
# my_random_number = random.randint(1, 10)

# print("I am thinking of a number bewteen 1 and 10")
# setnumber = my_random_number
# gn = 0
# while gn != setnumber:
#     gn = int(input("What's the number?"))
#     if gn > setnumber:
#         print(gn, " is too hight")
#     if gn < setnumber:
#         print(gn, " is too low")

# # print("Yes! You win!")

# import random
# my_random_number = random.randint(1, 10)

# print("I am thinking of a number bewteen 1 and 10")
# setnumber = my_random_number
# gn = 0
# attemps = 5
# while attemps == 0:
#     print (" you have ", attemps," guesse(s) left")

#     while gn != setnumber:
#         gn = int(input("What's the number?"))
#         if gn > setnumber:
#             print(gn, " is too hight")
#         if gn < setnumber:
#             print(gn, " is too low")

#     attemps -=1
    

# print("Yes! You win!")
# #NOT DONE



