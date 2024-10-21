# write your code here
from math import ceil

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

def decodeextra(word):
    lengte= ceil(len(word)/2)+3
    decoded = word[4:lengte]
    return decoded
'''
def decode5(sentence):
    start=0
    final=""
    space = sentence.find(" ")
    while space != -1:
        second=sentence[start:space]
        decoded = decodeextra(second)
        decoded = decode2(decoded)
        decoded = decode1(decoded)
        final+=decoded+" "
        start= space+1
        space = sentence.find(" ",start)  
    second=sentence[start:]
    decoded = decodeextra(second)
    decoded = decode2(decoded)
    decoded = decode1(decoded)
    final+=decoded+" "
    final= decode3(final[:-1])
    return final
    '''

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
    decoded = decodeextra(second)
    decoded = decode2(decoded)
    decoded = decode1(decoded)
    final+=decoded+" "
    final= decode3(final[:-1])
    return final

print(decode5("NBFOeWdu XfPAkkagtkzm CaxIkkrGaNprtOGYQszl fhmbdYeI YndYkdrUAVlLlqecnSZJQpxiklmJ"))
print(decode5("usXxnnaCvIBH aLabdxec VgklrGAXlnlOewnedAevYRQZHszQUUnk OOjErfAalbtzrNavpiGOPLAySDgd"))
print(decode5("IaaqeCmsOHTb ALdkwFirlrlUeqmaxLCSKnbF eLStdGabnYsMtYQXLPWZ BfRAdhen RsZstqajneggAzZMxROm"))
print(decode5("HrBMeaiHnfnXifWMnWlMpQpI vFwJtIhaekUZ uqlepRAVAkhbDeBA TUAIauntdMJq eilDtlixgDewrSFLIiSg nKEHlVApvGeGeqJG xcLUcPlxiImsbIitntgAPSCAKKerHMXI wUpBtnraekeGsUNXAwiA"))
print(decode5("URfJsLiShzteJjkb wJQmiNsT bqEPaC BrqIcJrhaEpHpVyzKNNKqfjw lzkXszeLnmtsexnfcKediLzPPyCdUdtw"))
print(decode5("bEAKsOeFcXnDaWtXsWmruqcfryizcaUcNQZNXgzscVUrvYhVsSxL UEgThhaavIevncab PXkZcuhuaanrgKegdySazGcarZGW"))

#Decode 3 should be last step and not first and decode 4 needed tweaks that weren't mentioned