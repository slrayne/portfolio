#!/usr/bin/python3

import hmac
import sys

def gen_tag(msg, key):
    hm = hmac.new(key.encode(),digestmod='md5')
    hm.update(msg.encode())
    return hm.hexdigest()

def usage():
    print("Usage: {} <msg> <name>".format(sys.argv[0]))

if __name__ == '__main__':
    filename = "master.key"
    
    with open(filename) as f:
        key = f.read()
    f.close()
    
    filename="tags.txt"
    
    with open(filename) as g:
        text = g.read()
        
    for line in text.split("\n"):
        if len(line) > 0:
            (msg,oldhash) = line.split(":")


            calcHash = gen_tag(msg, key)
            if (calcHash == oldhash):
                pass
            else:
                print(msg + ':' + calcHash + " | wrong:" + oldhash + "\n")