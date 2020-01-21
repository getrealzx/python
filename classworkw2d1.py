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

class Person:
    def __init__(self, name):
        self.name=name
        self.count=0        
    
    def greeting(self):
        print(f"Hello, {self.name}")
        self.count += 1
        
    
    def printCount(self):
        
        print(self.count)

sonny = Person("sonny")

sonny.greeting()
sonny.greeting()
sonny.greeting()
sonny.printCount()

#########################