#!/usr/bin/python3
for i in range(99):
    i = str(i)
    if len(i) == 1:
        i = '0' + i
    print("{}".format(i),end=", ")
print('99')