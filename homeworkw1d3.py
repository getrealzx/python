##Medium
# # 1.Multiply Vectors
# L1 = [2, 4, 5]
# L2 = [2, 3, 6]

# P =[]

# for i in range(len(L1)):
#     p = L1[i] * L2[i]
#     P.append(p)
# print(f'{L1} X {L2}  = {P}')
####################################

## 2. Matrix Addition
# x = [[1,3],[2,4]]

# y = [[5,2],[1,0]]

# s = [[0,0],[0,0]]

# for i in range(len(x)):
#     for i2 in range(len(y)):
#         s[i][i2] = x[i][i2] + y [i][i2]
# for r in s:
#     print(r)

# print(s)
# ####################################
# 



# ## 2.Matrix Addition II

# x = [[1,3,5],[2,4,6]]

# y = [[5,2,1],[1,0,7]]

# s = x.copy()

# outlen = (len(x))
# inlen = (len(x[0]))

# for i in range(outlen):
#     for n in range(inlen):
#         s[i][n] = x[i][n] + y[i][n]
# for r in s:
#     print(r)


##########################################

# list = [1,2,4,1,1,0]
# for i in list: 
#     print(i) 

#
#  #3.De-dup
# l = [1,3,3,9,3]
# nl = []


# for i in l:
#     if i not in nl:
#         nl.append(i)


# print(l)
# print(nl)
##########################################
# # 4. Leetspeak
# p = "I am a leet programmer"
# L = list(p)

# for i in range(len(L)):
#     if L[i].upper() == "A":
#         L[i] = "4"

#     if L[i].upper() == "E":
#         L[i] = "3"

#     if L[i].upper() == "G":
#         L[i] = "6"

#     if L[i].upper() == "I":
#         L[i] = "1"

#     if L[i].upper() == "O":
#         L[i] = "0"

#     if L[i].upper() == "S":
#         L[i] = "5"

#     if L[i].upper() == "T":
#         L[i] = "7"
        
# p = "".join(L)
# print(p)

# ##########################################

# 6. Long-long Vowels
# word = input("Please type a word to convert vowel to t if it is a long vowel  ")

# L = list(word)

# for i in range(1,len(L)):
#     if (L[i]==L[i-1] and (L[i]=="a" or L[i]=="e" or L[i]=="i" or L[i]=="o" or L[i]=="u")):
#         L[i] *= 3

# word = "".join(L)
# print(word)


# ##########################################
# 7. Caesar Cipher

# txt = "lbh zhfg hayrnea jung lbh unir yrnearq" # message
# alpha = "abcdefghijklmnopqrstuvwxyz"
# offset = int(input("Please input offset number  "))
# result = ""

# for char in txt:
#     # print(type(alpha.find(char)))
#     if char in alpha:
#         alpha_index = (alpha.find(char)-offset)%len(alpha)
#         result = result + alpha[alpha_index]
#     else:
#         result = result + char

# print(result)

