
from vigenere import removeNonAlphas, vigenere_encode, vigenere_decode
from permutation import perm_encrypt, perm_decrypt

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == "__main__":
    defaultplain = "Crypto is fast becoming my favorite course"
    defaultcipher = "RVCRZQHPARSUTKLXIDMBWFYIORSKTJAPRALJOKWT"
    defaultpw = "password"
    rounds = ""

    encrypt = " "

    while (not encrypt[0] in "DE"):
        encrypt = input("Do you want to [E]ncrypt or [D]ecrypt (choose a letter)? ").upper()

    
    rounds = input("How many rounds of encryption[1]? ")
    
    rounds = 1 if not rounds.isnumeric() else int(rounds)

    if encrypt[0] == "E":
        userinput = input("What do you want to encrypt[{}]? ".format(defaultplain))
    else:
        userinput = input("What would you like to decrypt[{}]".format(defaultcipher))

    if len(userinput) > 0:
        inputtext = removeNonAlphas(userinput)
    else:
        inputtext = removeNonAlphas(defaultplain) if encrypt[0] == "E" else defaultcipher

    password = input("Password[{}]? ".format(defaultpw))

    password = password.upper() if len(password) > 0 else defaultpw
    if encrypt[0] == "E":
        if len(inputtext) % len(password) != 0:
            inputtext += "X"*(len(password) - len(inputtext)%len(password))
            #padding = (len(password) - len(plaintext)%len(password))
            #plaintext += alphabet[padding]*padding
        ciphertext = ""
        for block in range(0,int(len(inputtext) / len(password))):
            start = int(block*len(password))
            stop = int(start + len(password))
            cipherblock = ""
            plainblock = inputtext[start:stop]
            print("Block {}".format(plainblock))
            for thisround in range(0,rounds):
                print("\tRound {:d}".format(thisround + 1))
                cipherblock = vigenere_encode(plainblock,password)
                print ("\t\tSubstitution Encrypt on {} gives {}".format(plainblock,cipherblock))
                plainblock = cipherblock
                cipherblock = perm_encrypt(cipherblock,password)
                print ("\t\tPermutation Encrypt on {} gives {}".format(plainblock,cipherblock))
                plainblock = cipherblock
            
            ciphertext += cipherblock
            
        print("\n\n{} \n=>\n {}\n\n".format(inputtext,ciphertext))
        print("In binary:")
        # using join() + bytearray() + format() 
        # Converting String to binary 
        res_in = ''.join(format(i, 'b') for i in bytearray(inputtext, encoding ='utf-8'))
        res_out = ''.join(format(i, 'b') for i in bytearray(ciphertext, encoding ='utf-8'))
        
        print("{} \n=>\n{}".format(str(res_in),str(res_out)))

    else:
        plaintext = ""
        for block in range(0,int(len(inputtext) / len(password))):
            start = int(block*len(password))
            stop = int(start + len(password))
            cipherblock = inputtext[start:stop]
            print("Block {}".format(cipherblock))
            for thisround in range(0,rounds):
                print("\tRound {:d}".format(thisround + 1))
                plainblock = perm_decrypt(cipherblock,password)
                print ("\t\tPermutation Decrypt on {} gives {}".format(cipherblock,plainblock))
                cipherblock = plainblock
                plainblock = vigenere_decode(plainblock,password)
                print ("\t\tSubstitution Decrypt on {} gives {}".format(cipherblock,plainblock))
                cipherblock = plainblock
            
            plaintext += plainblock
            
        print("\n\n{} \n=>\n {}\n\n".format(inputtext,plaintext))
        
        print("In binary:")
        # using join() + bytearray() + format() 
        # Converting String to binary 
        res_in = ''.join(format(i, 'b') for i in bytearray(inputtext, encoding ='utf-8'))
        res_out = ''.join(format(i, 'b') for i in bytearray(plaintext, encoding ='utf-8'))
        
        print("{} \n=>\n{}".format(str(res_in),str(res_out)))
    
    