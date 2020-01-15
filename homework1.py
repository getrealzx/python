
# #1. Tip Calculator


# bill = float(input("Total bill amount? "))
# lvlsvs = input("Level of Service? ")
# lvlsvs = lvlsvs.lower()
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

# #Tip Calculator 2


# bill = float(input("Total bill amount? "))
# lvlsvs = input("Level of Service? ")
# lvlsvs = lvlsvs.lower()
# n_ppl = int(input("Split how many ways? "
# ))

# percenttips = 0.1

# if lvlsvs == "good":
#     percenttips = 0.2
# elif lvlsvs == "fair":
#     percenttips = 0.15
# elif lvlsvs == "bad":
#     percenttips = 0.1

# tips = float("%.2f" %(percenttips * bill))
# total = bill + tips
# amount_per_person = float("%.2f" %(total / n_ppl))

# output = f"Tip amount is ${tips} \nTotal amount is ${total} \n Amount per person: ${amount_per_person}"

# print(output)
##########################

# #3. How many coins?

# answer = "yes"
# numcoin = 0

# while answer == "yes":
#     output = f"You have {numcoin} coins"
#     print(output)
#     answer = input("Do you want another? ")
#     answer = answer.lower()
#     if answer == "yes" :
#         numcoin += 1
#     else:
#         answer = "no"
#         print("Bye")

# #################################


# # 4. Print a Box
# width = int(input("Width? "))
# height = int(input("Height? "))
# w = 1
# h = 1

# while h <= height:
#     if h == 1 or h == height:
#         print("*"*width)
#     else:
#         print("*" + " "*(width-2) + "*")
#     h += 1

# ##########################################

# #5. Print a Triangle

# lvl = 1
# fspacer = 4

# while fspacer >0:
#     print(" "*fspacer + "*"*lvl)
#     fspacer -= 1
#     lvl += 2
#############################################

# # 6.Multiplication Table
# x = 1
# y = 1

# while x <=10:
#     while y <=10:
#         product = x*y
#         output = f'{x} X {y} = {product}'
#         y += 1
#         print(output)
#     y = 1
#     x += 1
    

# ############################################





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
#     gn = int(input("What's the number? "))
#     if gn > setnumber:
#         print(gn, " is too hight")
#     if gn < setnumber:
#         print(gn, " is too low")

# print("Yes! You win!")

######################################

# #Guess a number v3

# import random
# my_random_number = random.randint(1, 10)

# print("I am thinking of a number bewteen 1 and 10")
# setnumber = my_random_number
# gn = 0
# while gn != setnumber:
#     gn = int(input("What's the number? "))
#     if gn > setnumber:
#         print(gn, " is too hight")
#     if gn < setnumber:
#         print(gn, " is too low")

# print("Yes! You win!")
################################################

#### Limited Guesses
import random
my_random_number = random.randint(1, 10)

print("I am thinking of a number bewteen 1 and 10")
setnumber = my_random_number
gn = 0
attemps = 5
    

while gn != setnumber and attemps > 0:
    print (" you have ", attemps," guesse(s) left")
    gn = int(input("What's the number? "))
    if gn > setnumber:
        print(gn, " is too hight")
    if gn < setnumber:
        print(gn, " is too low")

    attemps -=1


if attemps < 1:
    print("You ran out of guesses!")
else:  
    print("Yes! You win!")

##################################################


