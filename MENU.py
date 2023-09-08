#!/usr/bin/python
def menu():
    print("Please select from the following menu options:")
    print("\t1. Add a new user")
    print("\t2. Modify an existing user")
    print("\t3. Change a user's role")
    print("\t4. Delete a user's role")
    print("\t5. Delete a user")
    print("\t6. Exit the system")

menu()
option = int(input("Enter your Option:"))
if option == 1:
             #this is going to add a user
    print(" You selected add a new user")
elif option == 2:
    print("You selected modify an existing user")
elif option == 3:
    print("You selected change a user's role")
elif option == 4:
    print("You selected delete a user's role")
elif option == 5:
    print("You selected delete a user")
elif option == 6:
    print("You selected exit the system")
else:
    print("invalid selection, please try again")
    
def menu():
    print("Please select from the following menu options:")
    print("\t1. Add a new user")
    print("\t2. Modify an existing user")
    print("\t3. Change a user's role")
    print("\t4. Delete a user's role")
    print("\t5. Delete a user")
    print("\t6. Exit the system")

