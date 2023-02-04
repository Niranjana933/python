# n =int(input())

# for i in range(n):
#     #print(i+1)
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#Reverse pattern
# n = int(input())
# for i in range(n, 0, -1):
#     #print(i)
#     for j in range(i+1):
#      print("*",end=" ")
#      print()


# n = int(input())

# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

#cross pattern loop

# n = int(input())

# for i in range(n):
#     for j in range(n):
#         #print(i,j,end="->")
#         if i == j or i+j == n-1:
#             print("*", end=" ")
#         # elif i+j == n-1:
#         #     print("*", end=" ")
#         else:
#             print(" ", end=" ")
        
#     print()

#left pattern using while loop


# n =int(input())

# i =1

# while n > 0:
#     print(i)
#     i+=1
#     j = i
#     while j > 0:
#         print("*", end=" ")
#         j -= 1
#     print()
#     i+=1    
#     n-=1

# n =int(input())

# while n > 0:
#     rem = n%10
#     print(rem)
#     n = int(n/10)

#Reversing number
#========================

n = int(input())
_sum = 0

while n > 0:
    rem = n%10
    _sum = _sum*10 + rem

    n = int(n/10)