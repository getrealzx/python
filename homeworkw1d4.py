#############################################
# 1. Madlib function


# def Madlib (n,s):
#     r = f"{n}'s favorit subject is {s}"
#     return r

# # def Madlib(): #with input
# #     n = input("Name ")
# #     s = input("Subject ")
# #     r = f"{n}'s favorit subject is {s}"
# #     # print(result)
# #     return r

# # result = Madlib()

# result = Madlib("Jenn", "science")

# print(result)
#############################################


#3. Fahrenheit to Celsius conversion

# def TempConv():
#     F = int(input("Please input Fahrenheit: "))
#     C = (F - 32) * 5/9
#     return C


# print(f'The tempperature in Celsius is {TempConv()}')

#############################################
#6. only_evens function

# print(2%2)


# def only_evens(l):
#     ev = []
#     for i in l:
#         if i%2 != 1:
#             ev.append(i)
#     return ev

# print(only_evens([11, 20, 42, 97, 23, 10]))


#############################################
#Medium 1. Find the smallest number
# def smallest():
#     sn = int()
#     L=[8, 1 , 2, 5, 5, -9, 199, -11]
#     for n in L:
#         if n <= sn:
#             sn = n
#     print(sn)
#     return(sn)

# smallest()
#############################################
#2. Find the largest number
# def largest():
#     ln = int()
#     L=[8, 1 , 2, 5, 5, -9, 199, -11]
#     for n in L:
#         if n >= ln:
#             ln = n
#     print(ln)
#     return(ln)

# largest()
#############################################
# 3. Find the shortest string
# def shortest():
#     L=["I", "don't know", "this is an issueeeeeeeeeeeeeeeeeee","ok","haada Do"]
#     i=0

#     for s in L:
#         # print(s)
#         for i in range(len(L)):
#             if len(s) >= len(L[i]):
#                 s = L[i]
            
#             # print(f'L[{i}] = {L[i]}')
            
#                 # print(f's = {s}')
            
#     print(f'The shortest string in the list is "{s}"')

#     return(s)

# shortest()
#############################################
#4. Find the longest string
# def longest():
#     L=["I", "don't know", "this is an issueeeeeeeeeeeeeeeeeee","ok","haada Do"]

#     for s in L:
#         for i in range(len(L)):
#             if len(s) <= len(L[i]):
#                 s = L[i]
            
#     print(f'The longest string in the list is "{s}"')
#     return(s)

# longest()
#############################################