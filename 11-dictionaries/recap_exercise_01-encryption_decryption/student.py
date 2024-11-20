# write your code here
from math import ceil
import random

def decode1(word):
    decoded = word.replace("A","o")
    return decoded

def decode2(word):
    decoded = word[::2]
    return decoded

def decode3(word):
    space= word.find(" ")
    first = word[0:space]
    decoded = first[::-1]
    return f"{decoded}{word[space:]}"

def decode4(word):
    lengte= ceil(len(word)/2)+2
    decoded = word[2:lengte]
    return decoded

def decode5(sentence):
    start=0
    final=""
    space = sentence.find(" ")
    while space != -1:
        second=sentence[start:space]
        decoded = decode1(second)
        decoded = decode2(decoded)
        decoded = decode4(decoded)
        final+=decoded+" "
        start= space+1
        space = sentence.find(" ",start)  
    second=sentence[start:]
    decoded = decode1(second)
    decoded = decode2(decoded)
    decoded = decode4(decoded)
    final+=decoded+" "
    final= decode3(final[:-1])
    return final

def encode1(word):
    encode = word.replace("o","A")
    return encode

def encode2(word):
    encoded=""
    for i in range(len(word)):        
        encoded+=word[i]
        encoded+=random.choice(["a","b","e","r","f","h"])
    return encoded

print("testing purposes"==decode2(encode2("testing purposes")))
print(encode2("testing"))