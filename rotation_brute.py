
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inputtext = input("What is the rotation ciphertext to brute force? ")



for count in range(0,26):
    outtext = ""
    for  lett in inputtext.upper():
        if lett in alphabet:
            outtext += alphabet[(alphabet.index(lett)-count)%26]
        
    print("{:2d}: {}".format(count,outtext))