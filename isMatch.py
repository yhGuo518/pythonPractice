import re

def isMatch(str, pattern):
    newpattern=re.sub(r'[^.*]',lambda m: re.escape(m.group()),pattern)
    newpattern = newpattern+'$'
    return re.match(newpattern,str)!=None
    
print(isMatch("aa","a"))
print(isMatch("aa","aa"))
print(isMatch("aaa","aa"))
print(isMatch("aa","a*"))
print(isMatch("aa",".*"))
print(isMatch("ab",".*"))
print(isMatch("aab","c*a*b"))
print(isMatch("aab","c*b*b"))
print(isMatch("ab@","a*b*@"))
