
#find only common numbers in two lists.
import random


a = random.sample(range(1,1000),100)
b = random.sample(range(1,1000),100)
#a = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set([i for i in a if i in b])

#alternative method
#for i in a:
#    if i in b and i not in c:
#        c.append(i)

#print(a)
#print(b)
print(c)
