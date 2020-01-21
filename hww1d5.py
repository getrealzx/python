#1. Phonebook dictionary

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict["Elizabeth"])
# ####################################
# 2. Nested dictionary
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
# print(len(ramit['friends']))
# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][1]['email'])
# print(ramit['friends'][1]['interests'][0])

# ####################################
#3. Friend counter

# ramit = {
# 'name': 'Ramit',
# 'email': 'ramit@gmail.com',
# 'interests': ['movies', 'tennis'],
# 'friends': [
#     {
#     'name': 'Jasmine',
#     'email': 'jasmine@yahoo.com',
#     'interests': ['photography', 'tennis']
#     },
#     {
#     'name': 'Jan',
#     'email': 'jan@hotmail.com',
#     'interests': ['movies', 'tv']
#     }
# ],
# }

# def countFriends(d):

#     d['friends_count']=len(ramit['friends'])
#     print(d)

# countFriends(ramit)

####################################
# # 1. Letter Summary
# letter_count = {}

# def letter_histogram(LC):
#     word=input("Please enter a word: ")
#     for l in word:
#         if l in LC:
#             LC[l] = LC[l]+1
#         else:
#             LC[l] = 1
   
#     print(LC)

# letter_histogram(letter_count)
####################################
# #2. Word Summary



# def word_histogram():
#     w_count = {}
#     w_c = 0
#     sentence = input("Please enter a sentence: ")
#     alphlist="abcdefghijklmnopqrstuvwxyz"
#     word_list=[]
#     word = ""

#     sen=sentence.lower()
#     for c in sen:
#         if c not in alphlist:
#             word_list.append(word)
#             word=''
#         else:
#             word = word + c
#     if word !="":
#             word_list.append(word)


#     for w in word_list:
#         if w in w_count:
#             w_count[w] = w_count[w] + 1
#             print(w)
            

#         else:
#             w_count[w] = 1

#     print(w_count)

# word_histogram()



####################################
    
##3. Sorting a histogram

# import operator
# LC = {}

# word=input("Please enter a word: ")

# for l in word:
#     if l in LC:
#         LC[l] = LC[l]+1
#     else:
#         LC[l] = 1

# sorted_w = sorted(LC.items(), key=operator.itemgetter(1), reverse=True)[:3]

# print(sorted_w)




######################################

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




