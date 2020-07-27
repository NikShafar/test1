from math import ceil
a = 20000
i = 0
while i < 5:
    a = a * 1.15
    i = i + 1
a = ceil (a * 100) / 100
print (a)


