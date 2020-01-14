# #first 100 triangle number
# count = 0
# tn = 1 #tn is triangle number
# while count < 100:
#     count +=1
#     tn = count*((count+1)/2)
#     print(tn)
# print("those are first 100 triangle numbers")

#Factor Numbers

asknum = input("please input a number >>")
x = int(asknum)
i = 1
print("the factor of", x, "are")
while i < x:
    if x % i ==0:
        print(i)
    i +=1
    


