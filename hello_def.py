#!/usr/bin/python3

def helloworld(def_variable):
   print("Hello "+ def_variable)
   return

name=input("What is your name? ")

helloworld(name)
###################################################################################
def helloworld(variable1, variable2, variable3):
    print("Hello " + variable1)
    print("I will call you " + variable2)
    print("bitch " + variable3)

if __name__ == "__main__":

    name=input("What is your name?")
    nick=input("What would you like your nickname to be?")
    haha=input("What shall we call you behind your back?")

helloworld(name, nick, haha)