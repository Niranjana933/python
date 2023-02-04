#Write a program to check a number is armstrong or not.
# n= int(input("Enter a number:"))
# sum = 0
# temp = n 
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
#     if n == sum:
#         print(n,"is an Armstrong number")
#     else:
#             print(n, "is not an Armstrong number")

#============================================= 
#write a program to print all the prime number between 1 to 100.

Number= 1
while(Number<=100):
    count = 0
    i=2
    while(i<=Number//2):
        if(Number%i==0):
            count=count+1
            break
        i=i+1
        if(count==0 and Number!=1):
            print("%d"%Number,end='')
            Number = Number+1