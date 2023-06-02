alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inputtext = input("What is the rotation ciphertext to encode? ")

rotation = ""
while not rotation.isnumeric():
    rotation = input("What is the rotation? ")
    
rotation = int(rotation)

outtext = ""

for lett in inputtext.upper():
    if lett in alphabet:
        outtext += alphabet[(alphabet.index(lett) + rotation)%26]
    
print (outtext)