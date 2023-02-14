filename="PandFsubstitutions.txt"
#filename = "ts1.txt"    #Uncomment this to specify a file - useful for testing with the same input file
mapper = {}   # Define an empty dictionary object

"""
The following mappings will allow you to modify the decoding process.
After you run a frequency analysis, you will have the most common letter in your
encoded text.  Suppose the letter Q is the most common letter in the encoded text. We
would expect that to be the letter E.  In the mapping below, change the E INSIDE
the mapper to a Q.  In other words, the first line would read:
mapper['Q']='E' and so on.  This key-value mapping defines the substitution, so this is saying map Q -> E.

Ensure that each letter only occurs once inside the brackets - each key-value mapping should occur only once. So the Q (second up from the bottom)
would need to change based on the change above.

"""
mapper['E']='E'    # Expected 12.7%
mapper['T']='T'    # Expected 9.1%
mapper['A']='A'    # Expected 8.2%
mapper['O']='O'    # Expected 7.5%
mapper['I']='I'    # Expected 7.0%
mapper['H']='H'    # Expected 6.7%
mapper['N']='N'    # Expected 6.3%
mapper['S']='S'    # Expected 6.1%
mapper['D']='D'    # Expected 6.0%
mapper['R']='R'    # Expected 4.3%

mapper['L']='L'    # Expected 1.0%
mapper['U']='U'    # Expected 2.8%
mapper['M']='M'    # Expected 2.8%
mapper['W']='W'    # Expected 2.4%
mapper['Y']='Y'    # Expected 2.4%

mapper['C']='C'    # Expected 2.2%
mapper['F']='F'    # Expected 2.0%
mapper['B']='B'    # Expected 2.0%
mapper['G']='G'    # Expected 1.9%
mapper['P']='P'    # Expected 1.5%

mapper['K']='K'    # Expected 1.0%
mapper['V']='V'    # Expected .8%
mapper['J']='J'    # Expected .15%
mapper['X']='X'    # Expected .15%
mapper['Q']='Q'    # Expected .1%
mapper['Z']='Z'    # Expected .07%

f=""

while (f=="" or f=="error"):  #NOTE: Filename cannot be "error"
    if filename=="":
        filename = input("What is the name of the file to open? ")
    try:
        f=open(filename)
    except:
        f="error"
        
intext = ""      
outtext = ""
for lett in f.read():
    if lett.upper() in mapper.keys():
        lett = lett.upper()
        intext += lett
        outtext += mapper[lett]
        
f.close()
print("Original Text",intext)
print("Decrypted Text",outtext)