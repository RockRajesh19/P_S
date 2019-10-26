'''
Created on Oct 14, 2019

@author: rajesh
'''

num = 153
temp = num
sum1 = 0

while (num > 0):
    rem = num % 10
    sum1 = sum1 + (rem * rem * rem)
    num = num // 10
if (temp == sum1):
    print("armstrong number")
else:
    print("not a armstrong number")
    
