#!/usr/bin/python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def removeNonAlphas(inputstring):
    outstring = ""
    for lett in inputstring:
        if lett.upper() in alphabet:
            outstring += lett.upper()
    return outstring

def vigenere_encode(pt,pw):
    pt = pt.upper()
    pw = pw.upper()
    ct = ""
    position = 0
    for lett in pt:
        if lett in alphabet:
            alphaindex = alphabet.index(lett)
            passindex = alphabet.index(pw[position])
            enclett = alphabet[(alphaindex + passindex) % 26]
            ct += enclett
            position += 1
            position = position % len(pw)
    return ct

def vigenere_decode(ct,pw):
    ct = ct.upper()
    pw = pw.upper()
    pt = ""
    position = 0
    for lett in ct:
        if lett in alphabet:
            alphaindex = alphabet.index(lett)
            passindex = alphabet.index(pw[position])
            declett = alphabet[(alphaindex - passindex) % 26]
            pt += declett
            position += 1
            position = position % len(pw)
    return pt

if __name__ == "__main__":
    
    defaultpassword = "password"

    inputtext = ""

    f=""

    while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
        filename = input("What is the name of the file to open? ")
        try:
            f=open(filename)
            inputtext = f.read()
        except:
            f="error"
    
    encrypt = " "

    while (not encrypt[0] in "DE"):
        encrypt = input("Do you want to [E]ncrypt or [D]ecrypt the file (choose a letter)? ").upper()


    password = input("Password [{}]? ".format(defaultpassword))

    password = password.upper() if len(password) > 1 else defaultpassword
    inputtext = removeNonAlphas(inputtext)

    outtext = ""
    plain = ""

    pos = 0
    
    if encrypt[0] == "E":
        outtext = vigenere_encode(inputtext,password)
    else:
        outtext = vigenere_decode(inputtext,password)
        
    for blocks in range(0,int(len(inputtext)/len(password)) + (0 if len(inputtext) % len(password) == 0 else 1)):
        start = blocks*(len(password))
        stop = blocks*len(password) + len(password)
        print("{} => {}".format(inputtext[start:stop],outtext[start:stop]))
        
    #print("{} \n=>\n {}".format(inputtext,outtext))
