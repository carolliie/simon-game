string = "abcdefgh"

def findStr(l):
    for chr in string:
        if l in string: return "chr in str"
        
        else: return "not in str"

print(findStr("c"))
