# #method 1 :
# name = input("Enter your name : ")
# email = input("Enter email : ")
#
# fl = open("freashertxt.txt", "w")
# fl.write(name+"#"+email)
# fl.close()
# print("Record added")



#
# #method 2 :
# name = input("enter your name : ")
# email = input("enter your email : ")
#
# with open("freashertxt.txt","a") as fl:
#     fl.write(name + "#" + email + "\n")
#
# i = 0
#
# while i <5:          # there are two ways for writing the increasing number i
#     i +=1
#     name = input("enter your name : ")
#     password = input("enter ")
#     with open("login.txt","a") as fl:                  # w for creating a new file
#      fl.write(name + " " +password + "\n")             # a for editing the file
#                                                        # r for reading only the file


i = 0

while  i <= 5:          # there are two ways for writing the increasing number i
    name = input("enter your name : ")
    password = input("enter ")
    with open("login.txt","a") as fl:                  # w for creating a new file
     fl.write(name + " " +password + "\n")             # a for editing the file
                                                       # r for reading only the file


#making accounts
#logins

#============================================= today's lecture








