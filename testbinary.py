mynumber = 5
output = ""
myvalue = mynumber
while (myvalue > 0):
    myremainder = myvalue % 2
    output = str(myremainder) + output
    myvalue = int(myvalue /2)
print(mynumber, " is ",output," in binary")
