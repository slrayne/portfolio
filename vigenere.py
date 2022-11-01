#!/usr/bin/python3
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
def removeNonAlphas(inputstring):
    outstring = ""
    for lett in inputstring:
        if lett.upper() in alphabet:
            outstring += lett.upper()
    return outstring

def vigenere_encode(pt,pw,verbose=False):
    pt = pt.upper()
    pw = pw.upper()
    ct = ""
    position = 0
    for lett in pt:
        if lett in alphabet:
            alphaindex = alphabet.index(lett)
            passindex = alphabet.index(pw[position])
            enclett = alphabet[(alphaindex + passindex) % 26]
            if verbose:
                print("{} ({:d}) + {} ({:d}) => {} ({:d})".format(lett,alphaindex,pw[position],passindex,enclett,alphabet.index(enclett)))
            ct += enclett
            position += 1
            position = position % len(pw)
    return ct

def vigenere_decode(ct,pw,verbose=False):
    ct = ct.upper()
    pw = pw.upper()
    pt = ""
    position = 0
    for lett in ct:
        if lett in alphabet:
            alphaindex = alphabet.index(lett)
            passindex = alphabet.index(pw[position])
            declett = alphabet[(alphaindex - passindex) % 26]
            if verbose:
                print("{} ({:d}) + {} ({:d}) => {} ({:d})".format(lett,alphaindex,pw[position],passindex,declett,alphabet.index(declett)))
            pt += declett
            position += 1
            position = position % len(pw)
    return pt

if __name__ == "__main__":

    defaultplain = "I like crypto"
    defaultcipher = "XLACTCJQETG"

    encrypt = " "

    while (not encrypt[0] in "DE"):
        encrypt = input("Do you want to [E]ncrypt or [D]ecrypt (choose a letter)? ").upper()

    if encrypt[0] == "E":
        userinput = input("What do you want to encrypt[I like crypto]? ")
    else:
        userinput = input("What would you like to decrypt[XLACTCJQETG]")
        
    if len(userinput) > 0:
        inputtext = removeNonAlphas(userinput)
    else:
        inputtext = defaultplain if encrypt[0] == "E" else defaultcipher

    password = input("Password[pass]? ")

    password = password.upper() if len(password) > 0 else "pass"

    outtext = vigenere_encode(inputtext,password,True) if encrypt[0] == "E" else vigenere_decode(inputtext,password,True)
            
    print (inputtext," => ",outtext)
