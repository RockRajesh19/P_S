'''
Created on Jun 22, 2019

@author: rajesh
'''

n = 10

if n > 1:
    for i in range(2, n//2):
        if (n % i) == 0:
            print("Given number is not a Not prime")
            break
    else:
        print("Given number is a Prime")
else:
    print("Given number is Not a Prime")
    

    