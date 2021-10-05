mystring = "Hi hello how are you?"

count = 0
vowels = "aeiou"

for character in mystring:
    if character in vowels:
        count += 1

print("There are",count, "vowels.")