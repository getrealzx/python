str1=input("input string 1: ")
str2=input("input string 2: ")

for i in str1:
    if i not in str2:
        print(f"{i} is not in str2.")

for i in str2:
    if i not in str1:
        print(f"{i} is not in str1")