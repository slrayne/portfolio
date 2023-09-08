import hashlib


if __name__ == "__main__":
    letters = "abcdefghijklmnopqrstuvwxyz"
    filename = "hashes.txt"
    try:
        f=open(filename)
        laura = f.read()
    except:
        f="error"

    hashes=[]

    hashes = laura.split("\n")

    for let1 in letters:
        for let2 in letters:
            for let3 in letters:
                for let4 in letters:
                    for let5 in letters:
                        testvalue = let1 + let2 + let3 + let4 + let5
                        hash_obj = hashlib.md5(testvalue.encode())
                        if hash_obj.hexdigest() in hashes:
                            print(testvalue, hash_obj.hexdigest())
