#n=int(input())
#if n%2 == 0:
  #print("f{n} is even")
#else:
 #print("f{n} is odd")

n=int(input())

if(n%3==0 and n%5==0):
     print(f"{n} is divisible by 3 & 5")
     if n%3==0:
        print(f"{n} is divisible by 3")
     if n%5==0:
            print(f"{n} is divisible by 5")