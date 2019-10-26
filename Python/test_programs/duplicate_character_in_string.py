'''
Created on Oct 19, 2019

@author: rajesh
'''


s = "Python Programming"
se = set(())
for x in s :
    count = 0
    for y in s :
        if x == y :
            count += 1
    if count > 1 :
        se.add(x)
print(se)
    