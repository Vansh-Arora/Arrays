
def reverseWord(s):
    #your code here
    revs = ""
    for i in range(len(s)-1,-1,-1):
        revs += s[i]
    return revs