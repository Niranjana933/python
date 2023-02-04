

def findl(n):
    c=0
    while n>0:
        c+=1
        n=int(n/10)

def findsum(n,l):
    s=0
    while n>0:
        r=n%10
        s+=(r**l)
        n=int(n/10)
    return s

def isArmstrong(n,s):
    if n==s:
        return True
    else:
        return False
    
def armstrongR(_range):
    for i in range(_range):
        n=i
        l=findl(n)
        s=findsum(n,l)
        if isArmstrong(n,s):
            print(i)
