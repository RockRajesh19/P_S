'''
Created on Jun 22, 2019

@author: rajesh
'''

n = 15

if n > 1:
    for i in range(2, n//2):
        if (n % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")