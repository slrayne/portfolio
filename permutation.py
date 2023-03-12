#!/usr/bin/python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def removeNonAlphas(inputstring):
    outstring = ""
    for lett in inputstring:
        if lett.upper() in alphabet:
            outstring += lett.upper()
    return outstring

def perm_encrypt(plaintext,password,verbose=False):
    temppass = password
    passsort = []
    for lett in sorted(password):
        i = temppass.index(lett)
        passsort.append(i)
        temppass = temppass[:i] + "." + temppass[i+1:]

    ciphertext = ""

    if len(plaintext) % len(password) != 0:
        plaintext += "X"*(len(password) - len(plaintext)%len(password))
        #padding = (len(password) - len(plaintext)%len(password))
        #plaintext += alphabet[padding]*padding

    for block in range(0,int(len(plaintext) / len(password))):
        start = int(block*len(password))
        stop = int(start + len(password))
        cipherblock = ""
        plainblock = plaintext[start:stop]
        pos = 0
        for lett in plainblock:
            cipherblock+= plainblock[passsort[pos]]
            pos = (pos +  1) % len(password)
            
        if verbose:
            print("{} => {} ".format(plainblock,cipherblock))
        ciphertext += cipherblock
        
    return ciphertext

def perm_decrypt(ciphertext,password,verbose=False):
    ciphertext = removeNonAlphas(ciphertext)

    temppass = password
    passsort = []
    for lett in sorted(password):
        i = temppass.index(lett)
        passsort.append(i)
        temppass = temppass[:i] + "." + temppass[i+1:]

    plaintext = ""

    for block in range(0,int(len(ciphertext) / len(password))):
        start = int(block*len(password))
        stop = int(start + len(password))
        plainblock = "."*len(password)
        cipherblock = ciphertext[start:stop]
        pos = 0
        for lett in cipherblock:
            plainblock = plainblock[:passsort[pos]] + lett + plainblock[passsort[pos]+1:]
            pos = (pos +  1) % len(password)
        if verbose:
            print("{} => {} ".format(cipherblock,plainblock))
        plaintext += plainblock
    return plaintext



if __name__ == "__main__":
    pt = "I like crypto"
    ct = "LYCIRIKETXXPXOXX"

    encrypt = " "

    while (not encrypt[0] in "DE"):
        encrypt = input("Do you want to [E]ncrypt or [D]ecrypt (choose a letter)? ").upper()

    if encrypt[0] == "E":
        userinput = input("What do you want to encrypt[I like crypto]? ")
    else:
        userinput = input("What would you like to decrypt[LYCIRIKETXXPXOXX]")

    if len(userinput) > 0:
        inputtext = removeNonAlphas(userinput)
    else:
        inputtext = removeNonAlphas(pt) if encrypt[0] == "E" else ct

    userpw = input("Password[password]? ")

    userpw = userpw.upper() if len(userpw) > 0 else "password"

    outtext = perm_encrypt(inputtext,userpw,True) if encrypt[0] == "E" else perm_decrypt(inputtext,userpw,True)
            
    print (inputtext," => ",outtext)
