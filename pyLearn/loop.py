#!/usr/bin/python
# i = 2
# while(i < 10):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): print (j, " BREAK "); break
#         j = j + 1; print (j, " NOW ");
#     if (j > i/j) : print (i, " prime")
#     i = i + 1
#     print (i, " is ");
#
# print("Good bye!")

# Table Print
last = 10
start = 1
table = 2
while (start <= last):
    var = table*start
    # 2 | 2
    while (start < var):
        print('*')
    start+=1

