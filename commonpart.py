
#find only common numbers in two lists.
import random

def random_list():
    return random.sample(range(1,1000),100)

def common_parts(a,b):
    return set([i for i in a if i in b])

a = random_list()
b = random_list()
c = common_parts(a,b)

#alternative method
#for i in a:
#    if i in b and i not in c:
#        c.append(i)

print(a)
print(b)
print(c)
