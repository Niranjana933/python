string = "a1b2c3d4e5f"
#  for i in range(len(string)-1,-1,-1):
#     print(string[i])
num, alpha = "", ""
for i in string:
    print(i, i.isdigit())
    if i.isdigit():
        num += i
    else:
        alpha += i
print(num, alpha)

number = int(num)
print(type(num),number, type(number))


