mylist = [1, 2, 3, 4, 5, 1]

# print(mylist.count(1))
# mylist.sort(reverse=True)
# print(mylist)

# def linearSearch(mylist, val):
#     for i in mylist:
#         if i == val:
#             return True
#     return False


def sort(mylist):
    for i in range(len(mylist)):
        print(mylist)
    for j in range(len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i], mylist[j] = mylist

mylist = [2, 5, 1, 3, 4]

sort(mylist)
print(mylist)            